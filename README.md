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
assets/site.css                   estilos de todas as páginas
assets/site.js                    calculadora, WhatsApp e interações
og.png                            imagem de compartilhamento 1200x630
robots.txt  sitemap.xml
build/                            gerador das páginas
```

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

Sem dependências — só Python 3. O comando reescreve as 8 páginas, o
`robots.txt` e o `sitemap.xml`.

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

## Antes de publicar

**Obrigatório**

- [ ] **Número do WhatsApp** — preencher a constante `WHATSAPP` no `<script>`,
      no formato `5551999990000`. Enquanto estiver vazia, os botões abrem um
      aviso mostrando a mensagem que enviariam, em vez de abrir o WhatsApp.
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

Arquivos estáticos — servem em qualquer lugar. Pelo GitHub Pages:

```
Settings → Pages → Source: Deploy from a branch → main / (root)
```

Depois apontar o DNS de `megagramas.com.br` para o GitHub Pages e habilitar
HTTPS em Settings → Pages → Custom domain.
