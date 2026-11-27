#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as páginas de megagramas.com.br.

    python3 build/build.py

Sem dependências. O conteúdo fica em build/dados.py e o corpo da home em
build/partes/home.html. Os arquivos gerados são sobrescritos — editar aqui,
não no HTML de saída.
"""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from dados import (SITE, MARCA, SLOGAN, ANOS, NAV, GRUPOS_FAQ, PERGUNTAS, MODELOS,
                   APLICACOES_HOME, APLICACOES_TEXTO, PRAZOS, PRECO_MINIMO, RAZAO_SOCIAL, NOME_FANTASIA, ANTES_DEPOIS,
                   CNPJ, EMAIL, WHATSAPP_EXIBIDO, COLAS, DEPOIMENTOS, NUMERO_CLIENTES, INSTITUCIONAL)

HOME_CORPO = open(os.path.join(AQUI, 'partes', 'home.html'), encoding='utf-8').read()
BLOCO_CALC = re.search(r'<!--CALC:INICIO-->(.*?)<!--CALC:FIM-->', HOME_CORPO, re.S).group(1)

ZAP_SVG = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
  '<path d="M12.04 2c-5.46 0-9.9 4.44-9.9 9.9 0 1.75.46 3.45 1.32 4.95L2.05 22l5.3-1.38a9.87 9.87 0 0 0 4.69 1.19h.01'
  'c5.46 0 9.9-4.44 9.9-9.9 0-2.64-1.03-5.13-2.9-7A9.82 9.82 0 0 0 12.04 2Zm5.8 14.06c-.25.69-1.44 1.32-1.99 1.36-.53.05'
  '-1.02.24-3.44-.72-2.9-1.14-4.74-4.1-4.88-4.29-.14-.19-1.17-1.55-1.17-2.96s.74-2.1 1-2.39c.26-.29.57-.36.76-.36l.54.01'
  'c.18.01.41-.07.64.49.24.57.8 1.98.87 2.13.07.14.12.31.02.5-.09.19-.14.31-.28.48-.14.17-.3.37-.42.5-.14.14-.29.29-.12.57'
  '.16.29.73 1.2 1.56 1.94 1.07.96 1.98 1.25 2.26 1.39.28.14.45.12.61-.07.17-.19.71-.83.9-1.11.19-.29.38-.24.64-.14.26.09'
  '1.66.78 1.95.93.28.14.47.21.54.33.07.12.07.69-.17 1.37Z"/></svg>')

def logo(base, altura, classe='', por_tema=True):
    """A folha da logo como imagem, e o nome em tipografia.

    A logo do cliente traz o nome em lettering creme e verde, desenhado para
    fundo branco. Em imagem, nenhuma das duas metades atravessa os dois fundos
    do site: o creme some no papel claro, e o verde do "GRAMAS" dá 3,4:1 no
    cabeçalho escuro e 2,3:1 no rodapé. Reduzido a 34px, o lettering de duas
    linhas ainda virava mancha.

    Escrever o nome em Archivo resolve os três de uma vez: a cor vem dos
    tokens do tema (pior caso 5,2:1), fica nítido em qualquer tamanho e custa
    zero byte. A folha continua sendo o arquivo original, em duas variantes,
    porque ela também tem uma metade clara e uma escura."""
    c, d = f'{base}assets/logo/marca-claro', f'{base}assets/logo/marca-escuro'
    if por_tema:
        fontes = (f'<source srcset="{d}.webp" media="(prefers-color-scheme: dark)" type="image/webp">'
                  f'<source srcset="{d}.png" media="(prefers-color-scheme: dark)">'
                  f'<source srcset="{c}.webp" type="image/webp">')
        src = f'{c}.png'
    else:
        fontes = f'<source srcset="{d}.webp" type="image/webp">'
        src = f'{d}.png'
    return (f'<picture>{fontes}'
            f'<img src="{src}" alt="" width="123" height="120" style="height:{altura}">'
            f'</picture>'
            f'<span class="marca-nome {classe}">MEGA<span>GRAMAS</span></span>')


# ---------------------------------------------------------------- componentes

def galeria_antes_depois(base, limite=None):
    """As imagens já trazem os rótulos ANTES/DEPOIS e a marca embutidos, então
    o site não acrescenta rótulo nenhum — só a legenda do espaço."""
    return '<div class="galeria-ad">' + ''.join(
        '<figure class="par-ad">'
        + foto_real(base, par['arq'], 'Antes e depois: ' + par['titulo'].lower(),
                    'foto-1x1', 760, 760)
        + f'<figcaption><strong>{par["titulo"]}</strong>'
          f'<span>{par["desc"]}</span></figcaption></figure>'
        for par in ANTES_DEPOIS[:limite]) + '</div>'


def foto_real(base, nome, alt, classe="foto-4x3", larg=900, altura=675):
    """Foto real do cliente: WebP na frente, JPEG atrás, carregamento preguiçoso."""
    return (f'<picture>'
            f'<source srcset="{base}assets/fotos/{nome}.webp" type="image/webp">'
            f'<img class="{classe} foto-real" src="{base}assets/fotos/{nome}.jpg" '
            f'alt="{alt}" loading="lazy" decoding="async" width="{larg}" height="{altura}">'
            f'</picture>')


def foto(legenda, titulo="Foto", classe="foto-4x3"):
    return (f'<div class="foto {classe}"><span class="tag"><b>{titulo}</b>{legenda}</span></div>')


def cabecalho(base, atual):
    itens = []
    for rotulo, destino in NAV:
        marca = ' aria-current="page"' if destino.split('#')[0] == atual else ''
        itens.append(f'<a href="{base}{destino}"{marca}>{rotulo}</a>')
    return f'''<header class="topo">
  <div class="wrap">
    <a class="marca" href="{base}index.html" aria-label="MegaGramas, página inicial">{logo(base, '40px')}</a>
    <nav>{''.join(itens)}</nav>
    <a class="btn btn-zap" href="#" data-zap="topo" aria-label="Solicitar orçamento pelo WhatsApp">{ZAP_SVG}<span>Orçamento</span></a>
  </div>
</header>'''


def rodape(base):
    nav = ''.join(f'<li><a href="{base}{d}">{r}</a></li>' for r, d in NAV)
    modelos = ''.join(f'<li><a href="{base}{m["slug"]}/index.html">{m["nome"]}</a></li>' for m in MODELOS)
    return f'''<footer>
  <div class="wrap">
    <div>
      <a class="marca" href="{base}index.html" style="margin-bottom:16px" aria-label="MegaGramas, página inicial">{logo(base, '44px', classe='marca-nome-rodape', por_tema=False)}</a>
      <p style="max-width:34ch">{SLOGAN}. Grama sintética para residências, empresas, playgrounds e áreas de lazer.</p>
    </div>
    <div><h4>Linhas</h4><ul>{modelos}</ul></div>
    <div><h4>Navegar</h4><ul>{nav}<li><a href="{base}politica-de-privacidade/index.html">Política de privacidade</a></li></ul></div>
  </div>
  <div class="wrap fim">
    <span>megagramas.com.br</span>
    <span>&copy; 2026 {MARCA}</span>
    <span>{SLOGAN}</span>
  </div>
</footer>'''


FAB_TOAST = f'''<button class="fab" id="fab" aria-label="Falar no WhatsApp">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{ZAP_SVG.split('>',1)[1].rsplit('</svg>',1)[0]}</svg>
</button>
<div class="toast" id="toast" hidden>
  <div class="t">Botão em modo demonstração — mensagem que será enviada</div>
  <div class="m" id="toast-msg"></div>
</div>'''


def faq_html(perguntas):
    return '<div class="faq">' + ''.join(
        f'<details><summary>{q["p"]}</summary><div class="resp">{q["r"]}</div></details>'
        for q in perguntas) + '</div>'


def migalhas(base, trilha):
    """trilha: lista de (rotulo, destino ou None para a página atual)."""
    partes = [f'<a href="{base}index.html">Início</a>']
    for rotulo, destino in trilha:
        partes.append('<span aria-hidden="true">/</span>')
        partes.append(f'<a href="{base}{destino}">{rotulo}</a>' if destino else f'<span>{rotulo}</span>')
    return '<nav class="migalhas" aria-label="Você está aqui">' + ''.join(partes) + '</nav>'


def ld_migalhas(trilha_urls):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(trilha_urls)]}


# ------------------------------------------------------------------- template

def pagina(caminho, titulo, desc, corpo, atual, jsonlds=(), base=None, arquivo=None, noindex=False):
    if base is None:
        base = '' if caminho == '' else '../'
    url = SITE + '/' + (caminho + '/' if caminho else '')
    robots = '\n<meta name="robots" content="noindex">' if noindex else ''
    blocos = ''.join(
        f'\n<script type="application/ld+json">\n{json.dumps(j, ensure_ascii=False, indent=2)}\n</script>'
        for j in jsonlds)
    doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo} | {MARCA}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">{robots}
<meta name="theme-color" content="#0F5C27">
<link rel="icon" type="image/png" sizes="32x32" href="{base}assets/logo/icone-32.png">
<link rel="apple-touch-icon" href="{base}assets/logo/icone-180.png">

<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{MARCA}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{titulo} | {MARCA}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">

<link rel="preload" as="font" type="font/woff2" crossorigin href="{base}assets/fontes/archivo-variavel-500-800.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{base}assets/fontes/karla-variavel-400-700.woff2">
<link rel="stylesheet" href="{base}assets/site.css">{blocos}
<style>
  :root{{ color-scheme: light dark; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
  html, body{{ margin:0; }}
  img{{ max-width:100%; }}
  [hidden]{{ display:none !important; }}
</style>
</head>
<body>

{cabecalho(base, atual)}

<main id="topo">
{corpo}
</main>

{rodape(base)}
{FAB_TOAST}
<script src="{base}assets/site.js"></script>
</body>
</html>
'''
    destino = os.path.join(RAIZ, arquivo) if arquivo else (
        os.path.join(RAIZ, caminho, 'index.html') if caminho else os.path.join(RAIZ, 'index.html'))
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, 'w', encoding='utf-8').write(doc.replace('{{BASE}}', base))
    return url


# --------------------------------------------------------------------- páginas

LD_NEGOCIO = {
  "@context": "https://schema.org", "@type": "LocalBusiness", "name": MARCA,
  "description": "Grama sintética sob medida para residências, empresas, playgrounds e áreas de lazer. Venda por m², orientação especializada e instalação conforme a região.",
  "url": SITE + "/", "slogan": SLOGAN, "image": SITE + "/og.png",
  "areaServed": {"@type": "Country", "name": "Brasil"}, "foundingDate": "2014",
  "knowsAbout": ["Grama sintética", "Grama sintética decorativa",
                 "Grama sintética para playground", "Instalação de grama sintética"],
  # TODO: telephone, address, geo, openingHours e sameAs quando o cliente informar
}

URLS = []


def amostra(m, classe='foto-16x9'):
    """Quando a linha ainda não tem foto de fibra, o card mostra a cor da linha
    e a altura. Não é uma foto fingindo ser foto: é um painel de cor, e some
    quando o arquivo da foto for nomeado em dados.py."""
    cores = m['cores']
    if len(cores) == 1:
        fundo = f'--c1:{cores[0]};--c2:{cores[0]};--c3:{cores[0]}'
    else:
        fundo = ';'.join(f'--c{i+1}:{c}' for i, c in enumerate(cores))
    nome_cor = m.get('cores_nomes', '')
    alt = m['altura'].replace('mm', '')
    return (f'<div class="amostra {classe} n{len(cores)}" style="{fundo}">'
            f'<span class="alt">{alt}<small>mm</small></span>'
            f'<span class="lbl">altura das fibras</span></div>')


def capa_modelo(m, classe='foto-16x9'):
    if m['foto']:
        return foto_real('{{BASE}}', m['foto'],
                         f'Close da fibra de grama sintética de {m["altura"]} de altura', classe)
    return amostra(m, classe)


def cards_modelos():
    """Os cards da home, gerados a partir de dados.py — assim o catálogo vive
    num lugar só e a home não pode divergir das páginas de modelo."""
    saida = []
    for m in MODELOS:
        chips = ''.join(f'<li>{d}</li>' for d in m['diferenciais'][:3])
        saida.append(
            '<article class="modelo">'
            + capa_modelo(m)
            + f'<div class="corpo"><p class="linha-tag">{m["linha"]}</p>'
              f'<h3>{m["nome"]}</h3>'
              f'<p class="indic">{m["indicacao"]}</p>'
              f'<ul class="chips">{chips}</ul>'
              f'<a class="btn btn-linha" href="{{{{BASE}}}}{m["slug"]}/index.html">'
              f'Ver detalhes<span class="sr-only"> da {m["nome"]}</span></a></div></article>')
    nota = ('<p class="aviso-modelos">Na dúvida entre duas linhas ou alturas, peça orientação pelo '
            'WhatsApp: a diferença aparece muito mais ao vivo do que em foto. '
            'O valor de cada modelo é informado no atendimento.</p>')
    return '<div class="modelos">' + ''.join(saida) + '</div>' + nota


def prova_html():
    """Credibilidade sem inventar nada: o número de clientes é real, os
    depoimentos só aparecem quando existirem em dados.DEPOIMENTOS, e até lá a
    seção mostra a forma como a Mega Gramas atende."""
    numeros = (f'<div class="numeros">'
               f'<div class="numero"><div class="v">{ANOS}</div><div class="k">anos de mercado</div></div>'
               f'<div class="numero"><div class="v">{NUMERO_CLIENTES}</div><div class="k">clientes satisfeitos</div></div>'
               f'</div>')
    if DEPOIMENTOS:
        cards = ''.join(
            f'<figure class="depo-card"><blockquote>{d["texto"]}</blockquote>'
            f'<figcaption><strong>{d["nome"]}</strong>'
            f'<span>{d["cidade"]} · {d["projeto"]}</span></figcaption></figure>'
            for d in DEPOIMENTOS)
        return numeros + f'<div class="depo">{cards}</div>'
    cards = ''.join(f'<div class="inst"><h3>{t}</h3><p>{d}</p></div>' for t, d in INSTITUCIONAL)
    return numeros + f'<div class="institucional">{cards}</div>'


def colas_html():
    cards = ''.join(
        f'<div class="cola"><h3>{c["nome"]}</h3>'
        f'<p class="rend"><span>Rendimento estimado</span><strong>{c["rendimento"]}</strong></p></div>'
        for c in COLAS)
    return f'<div class="colas">{cards}</div>'


def prazos_html():
    itens = ''.join(f'<li><span class="k">{regiao}</span><span class="v">{prazo}</span></li>'
                    for regiao, prazo in PRAZOS)
    return ('<div class="prazos"><h3>Prazo de entrega</h3>'
            f'<ul>{itens}</ul>'
            '<p class="obs">O frete é calculado conforme o destino e o tamanho do pedido. '
            'Também vendemos pelo Mercado Livre — nesse caso valem os prazos e os valores '
            'da plataforma.</p></div>')


def gerar_home():
    corpo = HOME_CORPO.replace('<!--CALC:INICIO-->', '').replace('<!--CALC:FIM-->', '')
    corpo = corpo.replace('{{HERO}}',
      foto_real('{{BASE}}', 'hero-jardim',
                'Jardim residencial com grama sintética ao entardecer',
                'foto-hero', 1400, 788))
    cards_ap = ''.join(
        '<div class="card-local">'
        + foto_real('{{BASE}}', a['foto'], a['legenda'], 'foto-4x3', 760, 570)
        + f'<h3>{a["nome"]}</h3></div>' for a in APLICACOES_HOME)
    corpo = corpo.replace('{{APLICACOES}}',
      f'<div class="grid-cards">{cards_ap}</div><p class="ad-legenda">{APLICACOES_TEXTO}</p>')
    corpo = corpo.replace('{{MODELOS}}', cards_modelos())
    corpo = corpo.replace('{{PRECO}}', PRECO_MINIMO)
    corpo = corpo.replace('{{PROVA}}', prova_html())
    corpo = corpo.replace('{{COLAS}}', colas_html())
    corpo = corpo.replace('{{ANTES_DEPOIS}}',
      galeria_antes_depois('{{BASE}}', limite=3)
      + '<p class="ad-legenda"><a class="btn btn-linha" href="{{BASE}}projetos/index.html">'
        'Ver todos os projetos</a></p>')
    corpo = corpo.replace('<div class="faixa-extra">', prazos_html() + '<div class="faixa-extra">')
    topo = [q for q in PERGUNTAS if q['top']]
    bloco = faq_html(topo) + (
      '<p style="margin-top:26px"><a class="btn btn-linha" href="{{BASE}}perguntas-frequentes/index.html">'
      f'Ver todas as {len(PERGUNTAS)} perguntas</a></p>')
    corpo = corpo.replace('{{FAQ_HOME}}', bloco)
    URLS.append((pagina('', "Grama Sintética sob Medida",
      "Grama sintética para jardins, varandas, playgrounds, condomínios e empresas. Calcule a metragem certa, "
      f"receba orientação para escolher o modelo e peça seu orçamento pelo WhatsApp. {ANOS} anos de mercado, entrega para todo o Brasil.",
      corpo, 'index.html', [LD_NEGOCIO]), '1.0'))


def gerar_calculadora():
    perguntas = [q for q in PERGUNTAS if q['p'] in (
        "É vendida por m²?", "Vocês fazem cortes sob medida?", "Como calculo quantos metros preciso?")]
    corpo = f'''<section class="pagina-hero">
  <div class="wrap">
    {migalhas('{{BASE}}', [("Calculadora de metragem", None)])}
    <h1>Calculadora de metragem de grama sintética</h1>
    <p class="lead">Informe a largura e o comprimento e veja a área do espaço, a quantidade de grama a comprar, quantos rolos você recebe e quanta cola de contato é necessária. O cálculo considera o rolo de 2&nbsp;m de largura.</p>
  </div>
</section>

<section class="calc" style="padding-top:clamp(36px,5vw,56px)">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Calcule agora</p>
      <h2>Quanto de grama eu preciso?</h2>
      <p class="lead">A grama é vendida por m² inteiro, mas vem em <strong>rolo de 2,00 m de largura</strong>. Por isso a conta não para em largura × comprimento: o espaço precisa ser coberto por faixas inteiras, e a última quase sempre sobra — é esse pedaço que costuma faltar no orçamento.</p>
    </div>
    {BLOCO_CALC}
  </div>
</section>

<section>
  <div class="wrap-s">
    <div class="sec-head">
      <p class="eyebrow">Como a conta funciona</p>
      <h2>Por que área ÷ 2 dá o número errado.</h2>
    </div>
    <div class="prosa">
      <p>A grama é vendida por metro quadrado inteiro, com venda mínima de 1&nbsp;m², mas não vem em placas: vem em rolo de <strong>2,00 m de largura e 25 m de comprimento</strong> (50&nbsp;m² por rolo completo), cortado na metragem que você pedir. Cada metro de comprimento do rolo equivale a 2&nbsp;m² de material.</p>
      <p>Por isso a área do espaço não define a compra. Um jardim de 7,5 m × 7 m tem 52,50&nbsp;m², mas para atravessar 7,5 m de largura são necessárias 4 faixas inteiras de 2 m, cada uma com 7 m de comprimento. São 56&nbsp;m² de grama — e a quarta faixa sobra 0,5 m para fora, que é o desperdício normal de qualquer corte. Comprar só os 52,50&nbsp;m² deixaria o espaço descoberto.</p>
      <h3>Três números diferentes</h3>
      <p>A calculadora separa o que costuma ser confundido: a <strong>área real</strong> do espaço, a <strong>grama estimada para a instalação</strong> (a área coberta por faixas inteiras) e a <strong>quantidade recomendada para compra</strong>, arredondada para cima em m² inteiros, porque não vendemos frações de metro quadrado.</p>
      <h3>O sentido das faixas muda o resultado</h3>
      <p>O mesmo espaço pode ser coberto em duas orientações, e elas quase nunca custam igual. A calculadora monta as duas, compara e recomenda a de melhor aproveitamento — levando em conta que emenda não é de graça: ela custa mão de obra e aparece no acabamento. Todas as faixas são assentadas no mesmo sentido das fibras.</p>
      <h3>Rolos e cola</h3>
      <p>Até 50&nbsp;m² você recebe um rolo cortado na metragem comprada; acima disso, rolos completos de 50&nbsp;m² mais um rolo com o restante. A cola de contato Quimicolla é estimada a partir do rendimento informado de cada embalagem, com uma alternativa de margem de segurança.</p>
      <h3>Quando o cálculo não basta</h3>
      <p>A calculadora assume um retângulo. Espaço em L, canteiro no meio, degrau, coluna, piscina ou qualquer recorte muda a conta — às vezes para menos, às vezes para bem mais. Nesses casos, envie as medidas e uma foto que a equipe calcula o aproveitamento real.</p>
      <div class="aviso" style="margin-top:22px"><strong>Uma observação sobre o sentido do fio.</strong> Todas as faixas precisam ser assentadas na mesma direção. Faixa invertida muda a forma como a luz bate na fibra e o trecho parece de outra cor, mesmo sendo o mesmo produto.</div>
    </div>
    <div class="cta-linha" style="margin-top:32px">
      <a class="btn btn-zap" href="#" data-zap="calculadora">{ZAP_SVG}Quero ajuda para calcular meu orçamento</a>
    </div>
  </div>
</section>

<section style="background:var(--surface-2)">
  <div class="wrap-s">
    <div class="sec-head"><p class="eyebrow">Sobre metragem</p><h2>Dúvidas frequentes.</h2></div>
    {faq_html(perguntas)}
  </div>
</section>'''
    ld = ld_migalhas([("Início", SITE + "/"), ("Calculadora", SITE + "/calculadora/")])
    URLS.append((pagina('calculadora', "Calculadora de Metragem de Grama Sintética",
      "Calcule a área, a quantidade de grama sintética a comprar, os rolos e a cola de contato do seu espaço. O cálculo é feito em faixas "
      "de 2 m — a largura do rolo — e não pela multiplicação simples da área, que dá material a menos.",
      corpo, 'calculadora/index.html', [ld]), '0.9'))


def gerar_modelo(m):
    outros = [o for o in MODELOS if o['slug'] != m['slug']]
    specs = ''.join(f'<li><span class="k">{k}</span><span class="v">{v}</span></li>' for k, v in m['specs'])
    aplic = ''.join(f'<li>{a}</li>' for a in m['aplicacoes'])
    dif = ''.join(f'<li>{d}</li>' for d in m['diferenciais'])
    resto = ''.join(f'<p>{t}</p>' for t in m['texto'][1:])
    rel = ''.join(
      f'<a class="rel" href="{{{{BASE}}}}{o["slug"]}/index.html"><span class="k">{o["linha"]}</span>'
      f'<h3>{o["nome"]}</h3><p>{o["indicacao"]}</p>'
      f'<span class="seta">Ver detalhes &rarr;</span></a>' for o in outros)
    comparacao = ''.join(
      f'<li><span class="k">{o["nome"]}</span><span class="v">{o["altura"]}</span></li>' for o in MODELOS)
    perguntas = [q for q in PERGUNTAS if q['g'] in ('escolha', 'instalacao')]
    desc = (m['texto'][0] + ' Consulte o valor e peça orientação pelo WhatsApp.')
    foto_html = capa_modelo(m)
    legenda = (f'<p class="legenda-foto">Fibra de {m["altura"]} vista de perto.</p>' if m['foto'] else '')
    corpo = f'''<section class="pagina-hero">
  <div class="wrap">
    {migalhas('{{BASE}}', [("Modelos", "index.html#modelos"), (m['nome'], None)])}
    <div class="duas-colunas">
      <div>
        <p class="eyebrow">{m['linha']} &middot; {m['altura']}</p>
        <h1 style="margin-top:14px">{m['nome']}</h1>
        <p class="lead">{m['texto'][0]}</p>
        <p class="indic-grande">{m['indicacao']}</p>
        <div class="cta-linha">
          <a class="btn btn-zap" href="#" data-zap="modelo" data-modelo="{m['nome']}">{ZAP_SVG}Pedir orçamento desta linha</a>
          <a class="btn btn-linha" href="{{{{BASE}}}}calculadora/index.html">Calcular metragem</a>
        </div>
      </div>
      <div>
        {foto_html}
        {legenda}
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="duas-colunas">
      <div>
        <div class="sec-head"><p class="eyebrow">Sobre a linha</p><h2>Para que tipo de espaço ela foi feita.</h2></div>
        <div class="prosa">{resto}</div>
        <h3 class="sub-titulo">Aplicações</h3>
        <ul class="aplic">{aplic}</ul>
        <h3 class="sub-titulo">Diferenciais</h3>
        <ul class="chips chips-grandes">{dif}</ul>
        <p class="fecho">{m['fecho']}</p>
      </div>
      <div class="ficha">
        <h3>Principais características</h3>
        <ul class="specs">{specs}</ul>
        <h3>Alturas das linhas</h3>
        <ul class="specs">{comparacao}</ul>
      </div>
    </div>
  </div>
</section>

<section class="calc">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Quanto comprar</p><h2>Calcule a metragem do seu espaço.</h2>
      <p class="lead">A grama é vendida por m², mas vem em rolo de largura fixa — então a quantidade a comprar depende de como as faixas cobrem a área. A calculadora estima a grama, os rolos e a cola.</p></div>
    {BLOCO_CALC}
  </div>
</section>

<section style="background:var(--surface-2)">
  <div class="wrap-s">
    <div class="sec-head"><p class="eyebrow">Antes de decidir</p><h2>Dúvidas sobre escolha e instalação.</h2></div>
    {faq_html(perguntas)}
    <p style="margin-top:26px"><a class="btn btn-linha" href="{{{{BASE}}}}perguntas-frequentes/index.html">Ver todas as {len(PERGUNTAS)} perguntas</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Outras linhas</p><h2>Compare com as demais.</h2></div>
    <div class="relacionados">{rel}</div>
  </div>
</section>'''
    ld = ld_migalhas([("Início", SITE + "/"), (m['nome'], f"{SITE}/{m['slug']}/")])
    URLS.append((pagina(m['slug'], f"{m['nome']} — Grama Sintética", desc, corpo,
                        m['slug'] + '/index.html', [ld]), '0.8'))


def gerar_projetos():
    reais = [
      ('projeto-padel', '500 m² para a área de circulação',
       'Empreendimento de padel em Espumoso/RS. A grama resolve a circulação entre as '
       'quadras — o piso de jogo é outro produto.', 820, 820),
      ('projeto-revenda', '320 m² instalados',
       'Revenda de veículos em Cachoeirinha/RS. Área interna de exposição, com circulação '
       'constante de clientes.', 820, 820),
    ]
    cards = ''.join(
      f'<figure class="projeto">'
      + foto_real('{{BASE}}', nome, legenda, 'foto-1x1', w, h)
      + f'<figcaption><strong>{legenda}</strong><span>{desc}</span></figcaption></figure>'
      for nome, legenda, desc, w, h in reais)
    corpo = f'''<section class="pagina-hero">
  <div class="wrap">
    {migalhas('{{BASE}}', [("Projetos realizados", None)])}
    <h1>Projetos realizados</h1>
    <p class="lead">{ANOS} anos instalando grama sintética em residências, condomínios,
    escolas, academias e empresas — principalmente em Porto Alegre e Região Metropolitana,
    e também no interior do Rio Grande do Sul e em Santa Catarina.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="projetos">{cards}</div>
  </div>
</section>

<section style="background:var(--surface-2)">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Antes e depois</p><h2>O mesmo espaço, duas fotos.</h2></div>
    {galeria_antes_depois('{{BASE}}')}
  </div>
</section>

<section>
  <div class="wrap-s">
    <div class="sec-head"><p class="eyebrow">Fale com a gente</p><h2>Quer um projeto como esses?</h2>
      <p class="lead">Mande as medidas e uma foto do espaço. A partir de
      R$ {PRECO_MINIMO} o m², com instalação em Porto Alegre e Região Metropolitana.</p></div>
    <div class="cta-linha">
      <a class="btn btn-zap" href="#" data-zap="projeto">{ZAP_SVG}Consultar meu projeto</a>
    </div>
  </div>
</section>'''
    ld = ld_migalhas([("Início", SITE + "/"), ("Projetos", SITE + "/projetos/")])
    URLS.append((pagina('projetos', "Projetos de Grama Sintética Realizados",
      f"Projetos de grama sintética instalados em residências, condomínios, escolas e empresas no Rio Grande do Sul. {ANOS} anos de mercado.",
      corpo, 'projetos/index.html', [ld]), '0.7'))


def gerar_faq():
    grupos = ''
    for chave, rotulo in GRUPOS_FAQ:
        doq = [q for q in PERGUNTAS if q['g'] == chave]
        grupos += f'<div class="faq-grupo"><h3>{rotulo}</h3>{faq_html(doq)}</div>'
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q['p'],
                              "acceptedAnswer": {"@type": "Answer", "text": q['r']}} for q in PERGUNTAS]}
    ld = ld_migalhas([("Início", SITE + "/"), ("Perguntas frequentes", SITE + "/perguntas-frequentes/")])
    corpo = f'''<section class="pagina-hero">
  <div class="wrap">
    {migalhas('{{BASE}}', [("Perguntas frequentes", None)])}
    <h1>Perguntas frequentes sobre grama sintética</h1>
    <p class="lead">As {len(PERGUNTAS)} perguntas que mais aparecem antes de uma compra — altura, instalação, limpeza, durabilidade, entrega e garantia.</p>
  </div>
</section>

<section>
  <div class="wrap-s">{grupos}
    <div class="aviso">Não achou a sua? Mande a pergunta pelo WhatsApp — se for útil para mais gente, ela entra nesta página.</div>
    <div class="cta-linha" style="margin-top:28px">
      <a class="btn btn-zap" href="#" data-zap="orientacao">{ZAP_SVG}Tirar uma dúvida pelo WhatsApp</a>
    </div>
  </div>
</section>'''
    URLS.append((pagina('perguntas-frequentes', "Perguntas Frequentes sobre Grama Sintética",
      "Altura, instalação sobre cimento ou terra, drenagem, limpeza, durabilidade, uso com animais, entrega e garantia. "
      "As dúvidas mais comuns sobre grama sintética, respondidas.",
      corpo, 'perguntas-frequentes/index.html', [ld_faq, ld]), '0.7'))


def gerar_privacidade():
    corpo = f'''<section class="pagina-hero">
  <div class="wrap-s">
    {migalhas('{{BASE}}', [("Política de privacidade", None)])}
    <h1>Política de privacidade</h1>
  </div>
</section>

<section>
  <div class="wrap-s">
    <div class="prosa">
      <p class="atualizado">Última atualização: 10 de outubro de 2026</p>

      <p>A {MARCA} é uma marca comercial operada por {RAZAO_SOCIAL}, nome fantasia
      {NOME_FANTASIA}, inscrita no CNPJ nº {CNPJ}, responsável pelo tratamento dos dados
      pessoais descritos nesta política.</p>

      <h2>1. Quais dados coletamos</h2>
      <p>O atendimento acontece pelo WhatsApp. Ao iniciar uma conversa a partir deste site,
      você normalmente informa nome, telefone, cidade, as medidas do espaço e fotos do local
      — o conteúdo que você mesmo decide enviar.</p>
      <p>A calculadora de metragem funciona inteiramente no seu navegador: as medidas que
      você digita não são enviadas para nós, a não ser que você mesmo as mande pelo WhatsApp.</p>
      <p>Este site não possui formulário de cadastro, não realiza compras ou pagamentos e
      não utiliza ferramentas de análise de audiência ou de publicidade. Caso isso mude,
      esta política será atualizada antes da ativação, com o respectivo painel de
      preferências de cookies.</p>

      <h2>2. Como utilizamos seus dados</h2>
      <p>Utilizamos os dados para responder dúvidas, preparar orçamentos, atender
      solicitações e dar continuidade ao relacionamento comercial. A negociação acontece
      pelos nossos canais de contato.</p>
      <p>Quando você autoriza separadamente, também utilizamos seus contatos para enviar
      promoções e novidades da {MARCA}. Essa autorização é opcional e pode ser retirada a
      qualquer momento, sem impedir o atendimento.</p>

      <h2>3. Compartilhamento de informações</h2>
      <p>Os dados podem ser tratados por fornecedores que apoiam o funcionamento do site, a
      hospedagem e o serviço de e-mail. O WhatsApp, operado pela Meta, trata as conversas
      conforme a política da própria plataforma.</p>
      <p>Caso o atendimento resulte em uma contratação, informações necessárias também
      poderão ser compartilhadas com prestadores envolvidos na entrega ou na instalação.
      Dados poderão ser fornecidos a autoridades quando houver obrigação legal.</p>

      <h2>4. Armazenamento e segurança</h2>
      <p>Conservamos os dados pelo período necessário ao atendimento, ao relacionamento
      comercial e ao cumprimento de obrigações legais ou exercício de direitos.</p>
      <p>Os contatos autorizados para promoções são utilizados enquanto essa finalidade
      permanecer válida ou até a retirada da autorização, ressalvadas as hipóteses legais
      de conservação.</p>
      <p>Adotamos medidas de proteção compatíveis com o tratamento realizado, como restrição
      de acesso e cuidados com as contas e sistemas utilizados.</p>

      <h2>5. Seus direitos</h2>
      <p>Você pode solicitar confirmação do tratamento, acesso e correção dos seus dados,
      informações sobre compartilhamento e, nas situações previstas em lei, exclusão,
      anonimização, bloqueio ou portabilidade.</p>
      <p>Também pode retirar seu consentimento e solicitar o cancelamento de mensagens
      promocionais. Algumas informações poderão ser conservadas quando houver fundamento
      legal para isso.</p>

      <h2>6. Contato</h2>
      <p>Para dúvidas sobre esta política, pedidos relacionados aos seus dados ou
      cancelamento de comunicações promocionais, entre em contato:</p>
      <ul>
        <li>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>WhatsApp: {WHATSAPP_EXIBIDO}</li>
      </ul>

      <h2>7. Atualizações</h2>
      <p>Esta política poderá ser atualizada para refletir mudanças no site ou no tratamento
      de dados. A versão vigente estará disponível nesta página, com a respectiva data de
      atualização.</p>
    </div>
  </div>
</section>'''
    ld = ld_migalhas([("Início", SITE + "/"), ("Política de privacidade", SITE + "/politica-de-privacidade/")])
    URLS.append((pagina('politica-de-privacidade', "Política de Privacidade",
      f"Como a {MARCA} coleta, usa, compartilha e protege dados pessoais de quem usa o site, conforme a LGPD.",
      corpo, 'politica-de-privacidade/index.html', [ld]), '0.2'))


def gerar_404():
    linhas = ''.join(
      f'<a class="rel" href="/{m["slug"]}/index.html"><span class="k">{m["linha"]}</span>'
      f'<h3>{m["nome"]}</h3><p>{m["indicacao"]}</p>'
      f'<span class="seta">Ver detalhes &rarr;</span></a>' for m in MODELOS)
    corpo = f'''<section class="pagina-hero">
  <div class="wrap-s">
    <p class="eyebrow">Erro 404</p>
    <h1 style="margin-top:14px">Essa página não existe.</h1>
    <p class="lead">O endereço pode ter mudado ou o link estar incompleto. Abaixo estão os caminhos mais usados — ou fale direto com a equipe.</p>
    <div class="cta-linha">
      <a class="btn btn-zap" href="#" data-zap="topo">{ZAP_SVG}Falar no WhatsApp</a>
      <a class="btn btn-linha" href="/index.html">Voltar para o início</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Linhas</p><h2>Talvez você procurasse uma destas.</h2></div>
    <div class="relacionados">{linhas}</div>
    <div class="relacionados" style="margin-top:14px">
      <a class="rel" href="/calculadora/index.html"><span class="k">Ferramenta</span><h3>Calculadora de metragem</h3><p>Quanta grama, quantos rolos e quanta cola o seu espaço pede</p><span class="seta">Calcular &rarr;</span></a>
      <a class="rel" href="/perguntas-frequentes/index.html"><span class="k">Dúvidas</span><h3>Perguntas frequentes</h3><p>Altura, instalação, limpeza, garantia e entrega</p><span class="seta">Ver &rarr;</span></a>
      <a class="rel" href="/projetos/index.html"><span class="k">Portfólio</span><h3>Projetos realizados</h3><p>Espaços entregues e depoimentos</p><span class="seta">Ver &rarr;</span></a>
    </div>
  </div>
</section>'''
    pagina('', "Página não encontrada",
      "A página procurada não existe. Veja as linhas de grama sintética, a calculadora de metragem e as perguntas frequentes.",
      corpo, '', base='/', arquivo='404.html', noindex=True)


def gerar_robots_sitemap():
    open(os.path.join(RAIZ, 'robots.txt'), 'w', encoding='utf-8').write(
      f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    itens = ''.join(
      f'  <url>\n    <loc>{u}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>{p}</priority>\n  </url>\n'
      for u, p in URLS)
    open(os.path.join(RAIZ, 'sitemap.xml'), 'w', encoding='utf-8').write(
      '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + itens + '</urlset>\n')


if __name__ == '__main__':
    gerar_home()
    gerar_calculadora()
    for m in MODELOS:
        gerar_modelo(m)
    gerar_projetos()
    gerar_faq()
    gerar_privacidade()
    gerar_404()
    gerar_robots_sitemap()
    print(f'{len(URLS)} páginas no sitemap (+ 404.html):')
    for u, p in URLS:
        print(f'  {p}  {u}')
    print('robots.txt e sitemap.xml atualizados.')
