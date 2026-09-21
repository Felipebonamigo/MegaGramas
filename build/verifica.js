#!/usr/bin/env node
/**
 * Verifica as páginas geradas contra um servidor HTTP local.
 *
 *   python3 -m http.server 8765 &
 *   node build/verifica.js http://localhost:8765
 *
 * Confere, em tema claro e escuro: erros de JavaScript, links internos
 * quebrados, rolagem horizontal a 390 px, um H1 por página, JSON-LD válido,
 * title/description/canonical presentes e acessibilidade WCAG 2.1 AA.
 * Sai com código 1 se algo reprovar.
 */
const { chromium } = require('playwright');
const fs = require('fs');

const BASE = (process.argv[2] || 'http://localhost:8765').replace(/\/$/, '');
const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');

const PAGINAS = ['index.html', 'calculadora/index.html', 'grama-decorativa/index.html',
  'grama-playground/index.html', 'grama-alto-trafego/index.html', 'projetos/index.html',
  'perguntas-frequentes/index.html', 'politica-de-privacidade/index.html', '404.html'];

const falhas = [];
const cacheLinks = new Map();

async function existe(url) {
  if (!cacheLinks.has(url)) {
    cacheLinks.set(url, fetch(url, { method: 'HEAD' }).then(r => r.ok).catch(() => false));
  }
  return cacheLinks.get(url);
}

(async () => {
  const navegador = await chromium.launch({
    executablePath: process.env.CHROMIUM_PATH || undefined,
  });

  for (const rel of PAGINAS) {
    for (const tema of ['light', 'dark']) {
      const p = await navegador.newPage({ viewport: { width: 390, height: 844 }, colorScheme: tema });
      const erros = [];
      p.on('pageerror', e => erros.push('JS: ' + e.message));
      p.on('console', m => { if (m.type() === 'error') erros.push('console: ' + m.text()); });
      p.on('requestfailed', r => erros.push('requisição falhou: ' + r.url().replace(BASE, '')));
      const externos = [];
      p.on('request', r => {
        const u = r.url();
        if (!u.startsWith(BASE) && !u.startsWith('data:') && !u.startsWith('about:')) externos.push(u);
      });

      const resp = await p.goto(`${BASE}/${rel}`, { waitUntil: 'networkidle' });
      if (!resp || !resp.ok()) falhas.push(`${rel}: servidor respondeu ${resp && resp.status()}`);
      await p.waitForTimeout(200);

      const info = await p.evaluate(() => ({
        h1: document.querySelectorAll('h1').length,
        titulo: document.title,
        desc: document.querySelector('meta[name="description"]')?.content || '',
        canonical: document.querySelector('link[rel="canonical"]')?.href || '',
        overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
        ld: [...document.querySelectorAll('script[type="application/ld+json"]')]
              .map(s => { try { return JSON.parse(s.textContent)['@type']; } catch (e) { return 'INVÁLIDO'; } }),
        hrefs: [...document.querySelectorAll('a[href]')].map(a => a.href),
      }));

      const p_ = (m) => falhas.push(`${rel} (${tema}): ${m}`);
      if (erros.length) p_(erros.join(' | '));
      if (info.h1 !== 1) p_(`${info.h1} elementos H1 (esperado 1)`);
      if (!info.titulo) p_('sem <title>');
      if (info.desc.length < 50) p_('meta description ausente ou curta demais');
      if (!info.canonical) p_('sem canonical');
      if (info.overflow > 0) p_(`rolagem horizontal de ${info.overflow}px a 390px`);
      if (info.ld.includes('INVÁLIDO')) p_('JSON-LD inválido');
      if (rel !== '404.html' && !info.ld.length) p_('sem JSON-LD');
      if (externos.length) p_('recurso de terceiros carregado: ' + [...new Set(externos)].join(', '));

      if (tema === 'light') {
        for (const h of [...new Set(info.hrefs)]) {
          if (!h.startsWith(BASE)) continue;
          if (!(await existe(h.split('#')[0]))) p_('link quebrado: ' + h.replace(BASE, ''));
        }
      }

      await p.addScriptTag({ content: AXE });
      const r = await p.evaluate(() => axe.run(document, {
        runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'] } }));
      for (const v of r.violations) {
        p_(`[${v.impact}] ${v.id}: ${v.nodes.slice(0, 2).map(n => n.target.join(' ')).join(', ')}`);
      }
      await p.close();
    }
  }

  // a calculadora precisa continuar acertando os casos-limite
  const p = await navegador.newPage();
  await p.goto(`${BASE}/calculadora/index.html`, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(250);
  const CASOS = [
    ['7,5', '7',  '28,00 m lineares', '3 emendas'],
    ['4',   '6',  '12,00 m lineares', '1 emenda'],
    ['2',   '10', '10,00 m lineares', 'Nenhuma — peça única'],
    ['1,5', '30', '30,00 m lineares', 'Nenhuma — peça única'],
    ['10',  '2,2','11,00 m lineares', '4 emendas'],
  ];
  for (const [l, c, linearEsperado, emendasEsperadas] of CASOS) {
    await p.fill('#ent-largura', l);
    await p.fill('#ent-comprimento', c);
    await p.waitForTimeout(80);
    const linear = (await p.locator('#res-linear').innerText()).trim();
    const emendas = (await p.locator('#res-emendas').innerText()).trim();
    if (linear !== linearEsperado || emendas !== emendasEsperadas) {
      falhas.push(`calculadora ${l} x ${c}: deu "${linear} / ${emendas}", esperava "${linearEsperado} / ${emendasEsperadas}"`);
    }
  }
  // e os botões precisam apontar para o WhatsApp configurado
  await p.evaluate(() => { window.__u = []; window.open = u => { window.__u.push(u); }; });
  await p.click('[data-zap="calculadora"]');
  const urls = await p.evaluate(() => window.__u);
  if (!urls.length || !/^https:\/\/wa\.me\/\d{12,13}\?text=/.test(urls[0])) {
    falhas.push('botão de WhatsApp não montou uma URL wa.me válida: ' + (urls[0] || 'nenhuma'));
  }
  await p.close();
  await navegador.close();

  if (falhas.length) {
    console.error(`\n${falhas.length} problema(s):\n`);
    falhas.forEach(f => console.error('  ✗ ' + f));
    process.exit(1);
  }
  console.log(`✓ ${PAGINAS.length} páginas verificadas em tema claro e escuro: sem erro de JavaScript,`);
  console.log('  sem link quebrado, sem rolagem horizontal, sem recurso de terceiros,');
  console.log('  JSON-LD e metadados presentes, WCAG 2.1 AA sem violações,');
  console.log(`  e a calculadora acerta os ${CASOS.length} casos-limite.`);
})();
