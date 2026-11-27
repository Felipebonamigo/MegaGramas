# megagramas.com.br

Site institucional da MegaGramas — grama sintética sob medida.

Página única em HTML, CSS e JavaScript, sem build e sem dependências.
Abrir `index.html` no navegador já mostra o site funcionando.

---

## O que já está pronto

As 13 seções do briefing, na ordem:

| # | Seção | Observação |
|---|---|---|
| 1 | Hero + CTA | Foto real de jardim |
| 2 | Faixa de benefícios | 5 ícones SVG desenhados à mão, sem biblioteca |
| 3 | Onde utilizar | 4 cards com foto + uma linha de texto para os demais ambientes |
| 4 | Por que escolher | 6 quebras de objeção + CTA |
| 5 | Modelos | Chamada "a partir de R$ 19,90 o m²" + 7 linhas, cada uma com página própria |
| 6 | Antes e depois | 3 pares na home; os 13 em `projetos/` |
| 7 | **Calculadora** | Área, grama a comprar, rolos e cola — ver abaixo |
| 8 | Como funciona | 5 passos |
| 9 | Confiança | 12 anos + "+500 clientes" + cartões institucionais; depoimentos reais entram por `DEPOIMENTOS` |
| 10 | Diferenciais | 6 itens + faixa complementar |
| 11 | Formas de atendimento | Material / material + instalação / projetos comerciais |
| 11b | Colas Quimicolla | 3 embalagens, rendimento estimado, sem preço; CTA para o WhatsApp |
| 12 | FAQ | 8 perguntas na home, 16 na página própria |
| 13 | CTA final | + botão flutuante de WhatsApp |

Também incluso: tema claro e escuro automático, layout responsivo até 390 px,
`LocalBusiness` e `FAQPage` em JSON-LD, Open Graph, favicon em SVG inline e
`canonical` apontando para `https://megagramas.com.br/`.

---

## Estrutura

Site estático de 13 páginas. Sem build obrigatório para visualizar — abrir
`index.html` no navegador já funciona.

```
index.html                          home
calculadora/                        calculadora + explicação do cálculo
mega-economica-10mm/                as 7 linhas, uma página cada,
mega-decor-12mm/                    geradas de MODELOS em dados.py
mega-plus-12mm/
mega-plus-mais-20mm/
mega-natural-garden-20mm/
mega-natural-garden-mais-32mm/
mega-color-12mm/
projetos/                           instalações e os 13 antes e depois
perguntas-frequentes/               as 16 perguntas, com FAQPage em JSON-LD
politica-de-privacidade/            política LGPD
404.html                            página de erro
assets/site.css                     estilos e @font-face de todas as páginas
assets/site.js                      calculadora, WhatsApp e interações
assets/fontes/                      Archivo, Karla e IBM Plex Mono (woff2)
og.png                              imagem de compartilhamento 1200x630
robots.txt  sitemap.xml
build/build.py                      gerador das páginas
build/dados.py                      conteúdo
build/partes/home.html              corpo da home
build/verifica.js                   verificação automatizada
```

**Atenção ao acrescentar uma linha ou página:** `deploy/publicar.sh` e
`build/empacota.sh` listam as pastas publicadas uma a uma (de propósito: só
vai ao ar o que está na lista). Página nova que não entra nessa lista é gerada,
commitada e não aparece no site.

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

Sem dependências — só Python 3. O comando reescreve as páginas do sitemap, a `404.html`,
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

O rolo tem **2,00 m de largura e 25 m de comprimento (50 m²)**, igual em todos
os modelos. A venda é por **m² inteiro, mínimo 1 m²** — sem frações. Por isso
largura × comprimento dá o número errado quase sempre: o espaço precisa ser
coberto por faixas inteiras de 2 m, e a última faixa sobra.

Exemplo, um espaço de 7,5 m × 7 m:

| | m² | Cobre o espaço? |
|---|---|---|
| Área real (largura × comprimento) | 52,50 | **Não** — falta a quarta faixa inteira |
| Grama para a instalação (4 faixas de 2 × 7 m) | 56,00 | Sim, 3 emendas |

A calculadora mostra três números distintos — área real, grama estimada para a
instalação e quantidade recomendada para compra (arredondada para cima, em m²
inteiros) —, mais os rolos, a cola e o aviso de que tudo é estimativa. Não
mostra preço em nenhum ponto: o valor sai pelo WhatsApp. O botão final envia
as medidas e todos os resultados na mensagem.

O algoritmo (`montar()`, `planejar()`, `rolos()` e `cola()` em `assets/site.js`):

1. Monta as duas orientações — faixas no sentido do comprimento e da largura.
2. Pontua cada uma por `metros lineares + emendas × 1,5`. O peso por emenda
   existe porque emenda custa mão de obra e aparece no acabamento.
3. Faixa maior que o rolo (25 m) conta uma emenda a mais no comprimento.
4. Recomenda a de menor pontuação e mostra a alternativa.
5. **Rolos:** de 1 a 50 m², um rolo cortado na metragem; acima, rolos completos
   de 50 m² mais um com o restante.
6. **Cola:** testa combinações de 14 kg, 2,8 kg e 700 g que cubram a área,
   preferindo poucas embalagens com pouca sobra (cada m² de sobra pesa 1/10 de
   embalagem). Reproduz os exemplos do cliente em rendimento máximo (10 m² →
   2 × 700 g; 50 m² → 2 × 2,8 kg; 100 m² → 1 × 14 kg; 120 m² → 14 kg + 2,8 kg)
   e mostra também a versão com margem de segurança, no rendimento mínimo
   (3, 20 e 60 m²).

Constantes no topo do `<script>`: `LARGURA_ROLO`, `COMPRIMENTO_ROLO`,
`PESO_EMENDA` e `COLAS`.

Casos conferidos pelo `verifica.js`:

| Espaço | Compra | Emendas | Por quê |
|---|---|---|---|
| 7,5 × 7 | 56 m² | 3 | 4 faixas de 7 m |
| 4 × 6 | 24 m² | 1 | fecha exato |
| 2 × 10 | 20 m² | peça única | uma faixa só |
| 1,5 × 30 | 60 m² | 1 | faixa de 30 m passa do rolo de 25 m: emenda no comprimento |
| 10 × 2,2 | 22 m² | 4 | evita desperdiçar 18 m² |

---

## Verificação

```
npm install
npx playwright install chromium
npm run serve &
npm run verifica
```

Abre as 13 páginas em tema claro e escuro, a 390 px de largura, e reprova se
encontrar: erro de JavaScript, link interno quebrado, rolagem horizontal,
requisição a terceiros, `H1` duplicado, `title`/`description`/`canonical`
faltando, JSON-LD inválido ou violação de WCAG 2.1 AA (via axe-core). Também
confere que a calculadora acerta os cinco casos-limite da tabela acima e que os
botões montam uma URL `wa.me` válida.

Roda no GitHub Actions a cada push (`.github/workflows/verifica.yml`), onde
também verifica se o HTML commitado bate com o que o gerador produz — é o que
pega alguém editando as páginas direto em vez de `build/dados.py`.

Resultado atual: as 13 páginas passam em tudo, sem nenhuma violação de
acessibilidade nos dois temas.

---

## Estado do conteúdo

**Confirmado pelo cliente**

- [x] **Largura do rolo: 2,00 m.** É a premissa de todo o cálculo de faixas —
      se mudar, todos os números da calculadora mudam junto.
- [x] **Catálogo (nov/2026), nomes e alturas oficiais, nesta ordem:** Mega
      Econômica 10mm, Mega Decor 12mm, Mega Plus 12mm, Mega Plus+ 20mm, Mega
      Natural Garden 20mm, Mega Natural Garden+ 32mm e Mega Color 12mm (azul,
      preto e vermelho). Substitui o catálogo de 12 / 20 / Real 30 mm. Os
      endereços antigos (`/grama-12mm/` etc.) redirecionam para `/#modelos`.
- [x] **Preço:** chamada única "Grama Sintética a partir de R$ 19,90 o m²".
      Sem preço individual por modelo nem nas colas.
- [x] **Garantia:** de 3 a 12 meses conforme o modelo. Só aparece no FAQ, não
      nas páginas de produto.
- [x] **Venda:** m² inteiro, mínimo 1 m²; rolo de 2 m × 25 m.
- [x] **Clientes:** "mais de 500 clientes satisfeitos" é real. A nota 4,9 e os
      depoimentos da prévia eram exemplos e **não** estão no site.
- [x] **Colas Quimicolla:** autorizado usar nome, marca e imagens; embalagens
      de 700 g (3 a 5 m²), 2,8 kg (20 a 30 m²) e 14 kg (60 a 100 m²).
- [x] **Região:** instalação em Porto Alegre e Região Metropolitana, mais RS e
      SC mediante consulta; entrega para todo o Brasil.
- [x] **As 16 respostas do FAQ**, revisadas pelo cliente.
- [x] **Política de privacidade** com razão social, CNPJ e e-mail reais.
- [x] **WhatsApp** `5551999694547`, em `assets/site.js`.

**Ainda falta**

- [ ] **Fotos de fibra de 4 linhas:** Mega Econômica 10mm, Mega Decor 12mm,
      Mega Natural Garden 20mm e Mega Color 12mm usam hoje um painel de cor com
      a altura, não foto. As outras três usam os closes existentes
      (`fibra-12mm` → Mega Plus 12mm, `fibra-20mm` → Mega Plus+ 20mm e
      `fibra-real30` → Mega Natural Garden+ 32mm) — **o cliente precisa confirmar
      que cada close corresponde a essa linha**.
- [ ] **Imagens e texto oficial das colas Quimicolla:** a seção usa só o nome e
      os rendimentos informados; falta a descrição do fabricante e as fotos
      das embalagens.
- [ ] **Depoimentos reais:** com autorização de quem falou, entram em
      `DEPOIMENTOS` (`dados.py`) e a seção troca sozinha o bloco institucional
      por eles. Nota de avaliação só se for medida.
- [ ] **Quatro ambientes sem foto** (varanda, condomínio, recepção comercial,
      entorno de quadra): aparecem como uma linha de texto, sem card.
- [ ] **Mercado Livre:** a loja existe e o site não menciona além do prazo.
- [ ] **Grama esportiva:** em desenvolvimento. Decidir se ganha um "em breve".

Publicadas: hero, 4 cards de ambiente, 3 closes de fibra, 2 instalações com
metragem e os 13 pares de antes e depois.

**Depois de publicar**

- [ ] GA4 e Meta Pixel. No dia em que entrarem, a política de privacidade
      precisa voltar a descrever cookies, Google Analytics e Pixel — o texto
      original do cliente já traz esses parágrafos prontos. Hoje a política
      descreve o site como ele é: atendimento por WhatsApp, sem formulário,
      sem analytics.
- [ ] Conversão do Google Ads no clique de cada botão de WhatsApp — cada botão
      já envia uma mensagem diferente (`MENSAGENS` no script), então dá para
      saber qual seção gerou o contato mesmo sem ferramenta de analytics.
- [ ] Páginas por cidade, que é o que faz o site ranquear em busca local.

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

O script compara o que está **publicado** (registrado em
`/var/lib/megagramas/versao`) com o `origin/main`, e sai cedo quando são
iguais — então rodar de 5 em 5 minutos não reescreve arquivos nem enche o
journal. `bash deploy/publicar.sh --forcar` ignora a checagem.

A comparação não pode ser entre o HEAD do repositório e o `origin/main`: quem
atualizar o repositório na mão sem publicar faria o script concluir que não há
trabalho, e o site ficaria para trás em silêncio.

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
