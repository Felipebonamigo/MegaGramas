# megagramas.com.br

Site institucional da MegaGramas — grama sintética sob medida.

Página única em HTML, CSS e JavaScript, sem build e sem dependências.
Abrir `index.html` no navegador já mostra o site funcionando.

---

## O que já está pronto

As 13 seções do briefing, na ordem:

| # | Seção | Observação |
|---|---|---|
| 1 | Hero + CTA | Foto de aplicação real (não rolo) — slot reservado |
| 2 | Faixa de benefícios | 5 ícones SVG desenhados à mão, sem biblioteca |
| 3 | Onde utilizar | 7 cards |
| 4 | Por que escolher | 6 quebras de objeção + CTA |
| 5 | Modelos | 3 linhas, cada uma com página própria + CTA |
| 6 | Antes e depois | Par de slots, mesmo ângulo |
| 7 | **Calculadora de metragem** | Ver abaixo |
| 8 | Como funciona | 5 passos |
| 9 | Provas e projetos | 12 anos + 2 números a preencher + galeria + depoimentos |
| 10 | Diferenciais | 6 itens + faixa complementar |
| 11 | Formas de atendimento | Material / material + instalação / projetos comerciais |
| 12 | FAQ | 8 perguntas na home, 16 na página própria |
| 13 | CTA final | + botão flutuante de WhatsApp |

Também incluso: tema claro e escuro automático, layout responsivo até 390 px,
`LocalBusiness` e `FAQPage` em JSON-LD, Open Graph, favicon em SVG inline e
`canonical` apontando para `https://megagramas.com.br/`.

---

## Estrutura

Site estático de 8 páginas. Sem build obrigatório para visualizar — abrir
`index.html` no navegador já funciona.

```
index.html                        home (a landing page do briefing)
calculadora/                      calculadora + explicação do cálculo
grama-decorativa/                 linha 12 a 25 mm
grama-playground/                 linha 25 a 40 mm
grama-alto-trafego/               linha 12 a 20 mm
projetos/                         galeria, antes e depois, depoimentos
perguntas-frequentes/             as 16 perguntas, com FAQPage em JSON-LD
politica-de-privacidade/          rascunho LGPD, com campos a preencher
404.html                          página de erro (o GitHub Pages usa esse nome)
assets/site.css                   estilos e @font-face de todas as páginas
assets/site.js                    calculadora, WhatsApp e interações
assets/fontes/                    Archivo, Karla e IBM Plex Mono (woff2)
og.png                            imagem de compartilhamento 1200x630
robots.txt  sitemap.xml
build/build.py                    gerador das páginas
build/dados.py                    conteúdo
build/partes/home.html            corpo da home
build/verifica.js                 verificação automatizada
```

O site não faz **nenhuma requisição a terceiros**. As fontes são
auto-hospedadas em `assets/fontes/` (102 KB, Archivo e Karla em versão
variável), o que evita o bloqueio de renderização do Google Fonts e impede que
o IP de cada visitante seja enviado para o Google.

### Como editar

**O HTML das páginas é gerado — não edite direto, será sobrescrito.**

| O que mudar | Onde | Depois |
|---|---|---|
| Textos, perguntas do FAQ, modelos | `build/dados.py` | rodar o build |
| Conteúdo da home | `build/partes/home.html` | rodar o build |
| Estrutura das páginas, SEO, JSON-LD | `build/build.py` | rodar o build |
| Estilos | `assets/site.css` | nada |
| Calculadora e interações | `assets/site.js` | nada |

```
python3 build/build.py
```

Sem dependências — só Python 3. O comando reescreve as 8 páginas, a `404.html`,
o `robots.txt` e o `sitemap.xml`.

A home é gerada a partir de `build/partes/home.html`, que é um fragmento com
dois marcadores: `{{BASE}}` (resolvido para o caminho relativo da página) e
`{{FAQ_HOME}}` (onde entram as perguntas marcadas com `top=True` em
`dados.py`). O bloco da calculadora fica entre `<!--CALC:INICIO-->` e
`<!--CALC:FIM-->` e é reaproveitado nas outras páginas a partir dali, então
existe em um lugar só.

O FAQ é HTML estático, gerado no build e não injetado por JavaScript — é o que
permite que o Google leia as perguntas.

---

## A calculadora

O rolo tem **2,00 m de largura fixa** e é vendido por metro linear. Por isso
área ÷ 2 dá o número errado quase sempre: a área precisa ser coberta por
faixas inteiras de 2 m, e a última faixa sobra.

Exemplo real, um espaço de 7,5 m × 7 m:

| | Metros lineares | Cobre a área? |
|---|---|---|
| Área ÷ 2 (como fazem os concorrentes) | 26,25 m | **Não** — faltam 3,5 m² |
| Cálculo por faixas (este site) | 28,00 m | Sim — 4 faixas de 7 m, 3 emendas |

O algoritmo (`montar()` e `planejar()` em `index.html`):

1. Monta as duas orientações possíveis — faixas no sentido do comprimento e no
   sentido da largura.
2. Pontua cada uma por `metros lineares + emendas × 1,5`. O peso por emenda
   existe porque emenda custa mão de obra e aparece no acabamento: sem ele, o
   cálculo sugeriria 15 faixas num corredor de 1,5 m × 30 m em vez de uma peça
   única.
3. Recomenda a de menor pontuação e mostra a alternativa de forma transparente.
4. Desenha as faixas, as emendas e a sobra de corte em SVG, em tempo real.

Constantes no topo do `<script>`: `LARGURA_ROLO`, `LINEAR_POR_VOLUME` e
`PESO_EMENDA`.

Casos conferidos:

| Espaço | Resultado | Por quê |
|---|---|---|
| 7,5 × 7 | 28,00 m · 3 emendas · 3,50 m² de sobra | 4 faixas de 7 m |
| 4 × 6 | 12,00 m · 1 emenda · sem sobra | fecha exato |
| 2 × 10 | 10,00 m · peça única | uma faixa só |
| 1,5 × 30 | 30,00 m · peça única | evita 14 emendas num corredor |
| 10 × 2,2 | 11,00 m · 4 emendas · sem sobra | evita desperdiçar 18 m² |

---

## Verificação

```
npm install
npx playwright install chromium
npm run serve &
npm run verifica
```

Abre as 9 páginas em tema claro e escuro, a 390 px de largura, e reprova se
encontrar: erro de JavaScript, link interno quebrado, rolagem horizontal,
requisição a terceiros, `H1` duplicado, `title`/`description`/`canonical`
faltando, JSON-LD inválido ou violação de WCAG 2.1 AA (via axe-core). Também
confere que a calculadora acerta os cinco casos-limite da tabela acima e que os
botões montam uma URL `wa.me` válida.

Roda no GitHub Actions a cada push (`.github/workflows/verifica.yml`), onde
também verifica se o HTML commitado bate com o que o gerador produz — é o que
pega alguém editando as páginas direto em vez de `build/dados.py`.

Resultado atual: as 9 páginas passam em tudo, sem nenhuma violação de
acessibilidade nos dois temas.

---

## Antes de publicar

**Obrigatório**

- [x] ~~**Número do WhatsApp**~~ — configurado: `5551999694547` (51 99969-4547),
      na constante `WHATSAPP` em `assets/site.js`. Os 8 pontos de entrada
      abrem o WhatsApp com mensagens distintas por seção.
- [ ] **Fotos** — todo bloco verde texturizado é um slot; a legenda diz qual
      foto entra. Serve como lista de produção.
- [ ] **Revisar as respostas do FAQ** — são rascunhos e estão marcados como
      tal na página. Remover o `<span class="rascunho">` depois de aprovar.
- [ ] **Conferir as especificações dos modelos** — as alturas são faixas de
      mercado, não o catálogo real.
- [ ] Remover a barra "Rascunho para revisão" do topo (`<div class="notas">`).

**Falta definir**

- [ ] Região de atendimento (cidade e estado) — decisivo para busca local
- [ ] Faixa de preço por m²
- [ ] Prazo de entrega e frete
- [ ] Números de prova: projetos realizados e m² instalados
- [ ] Imagem de compartilhamento 1200×630 (`og.jpg`)
- [ ] Política de privacidade — exigida para anunciar no Google e no Meta

**Depois de publicar**

- [ ] GA4 e Meta Pixel
- [ ] Conversão do Google Ads no clique de cada botão de WhatsApp — cada botão
      já envia uma mensagem diferente (`MENSAGENS` no script), então dá para
      saber qual seção gerou o contato mesmo sem ferramenta de analytics
- [ ] Páginas por modelo e por cidade, que é o que faz o site ranquear além da
      home

---

## Publicar

O site roda num VPS da Hostinger (Ubuntu 22.04), servido pelo **Caddy** a
partir de `/var/www/megagramas`. O repositório fica clonado em
`/opt/megagramas`.

O VPS já rodava Caddy na porta 80 como proxy reverso de outros serviços, então
o site entra nele em vez de subir um nginx concorrente. O Caddy emite e renova
o certificado HTTPS sozinho — **não use certbot**. A configuração de nginx fica
guardada em `deploy/` para o caso de o site mudar de servidor.

### Atualizar o site

Nada a fazer: um timer do systemd verifica a cada 5 minutos se há commit novo
na `main` e publica sozinho. Um merge na `main` chega ao ar em até 5 minutos.

Para forçar na hora:

```
systemctl start megagramas-publicar.service
```

Para acompanhar:

```
systemctl list-timers megagramas-publicar.timer
journalctl -u megagramas-publicar -n 30 --no-pager
```

O script sai cedo quando o SHA da `main` não mudou e o site já está no lugar,
então rodar de 5 em 5 minutos não reescreve arquivos nem enche o journal.
`bash deploy/publicar.sh --forcar` ignora essa checagem.

### Instalação inicial

```
apt install -y python3 git rsync
git clone https://github.com/Felipebonamigo/MegaGramas.git /opt/megagramas

# o site entra no Caddy que já roda no servidor
cp /opt/megagramas/deploy/megagramas.caddy /etc/caddy/conf.d/megagramas.caddy
caddy validate --config /etc/caddy/Caddyfile && systemctl reload caddy

# publicação automática
cp /opt/megagramas/deploy/megagramas-publicar.{service,timer} /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now megagramas-publicar.timer
```

Se o Caddyfile principal não tiver `import conf.d/*`, cole o conteúdo de
`deploy/megagramas.caddy` no fim dele.

O Caddy emite e renova o certificado HTTPS sozinho — **não use certbot**.

### Arquivos de deploy

| Arquivo | Para quê |
|---|---|
| `deploy/megagramas.caddy` | **em uso** — configuração do Caddy: 404, redirect de www, gzip, cache, cabeçalhos, HTTPS automático |
| `deploy/megagramas.nginx.conf` | equivalente para nginx, se o site mudar de servidor |
| `deploy/publicar.sh` | atualiza o site no servidor a partir do git |
| `deploy/megagramas-publicar.service` + `.timer` | publicação automática a cada 5 minutos |
| `deploy/megagramas.htaccess` | equivalente para Apache, se um dia o site for para hospedagem compartilhada |
| `build/empacota.sh` | gera um zip para upload manual, quando não houver acesso a shell |

### Notas de configuração

O cache de CSS e JS está em uma hora de propósito: os arquivos não têm hash de
versão no nome, então um cache longo faria uma atualização demorar dias para
chegar a quem já visitou. Quando o conteúdo estabilizar, vale subir esse valor
no bloco do nginx.

As fontes vão a um ano com `immutable`, porque o conteúdo delas nunca muda.

O HTML não é cacheado, senão uma correção de texto não aparece.
