#!/usr/bin/env bash
# Publica o site no VPS. Rodar NO SERVIDOR:
#
#   bash /opt/megagramas/deploy/publicar.sh            # publica se houver novidade
#   bash /opt/megagramas/deploy/publicar.sh --forcar   # publica de qualquer jeito
#
# Normalmente quem chama é o timer megagramas-publicar.timer, de 5 em 5
# minutos. Busca a última versão de main, regera as páginas e sincroniza
# apenas os arquivos públicos para /var/www/megagramas.

# As chaves fazem o bash ler o arquivo inteiro antes de executar. Sem isso,
# o `git reset` abaixo trocaria este próprio script no disco no meio da
# execução, e o bash continuaria lendo do ponto onde parou — em outro
# arquivo.
{
set -euo pipefail

REPO="${REPO:-/opt/megagramas}"
DESTINO="${DESTINO:-/var/www/megagramas}"
ESTADO="${ESTADO:-/var/lib/megagramas}"
MARCA="$ESTADO/versao"

cd "$REPO"
git fetch --quiet origin main
NOVO=$(git rev-parse origin/main)
PUBLICADO=$(cat "$MARCA" 2>/dev/null || echo "-")

# A comparação é entre o que está PUBLICADO e o que está em origin/main.
# Comparar o HEAD do repositório com origin/main não serve: quem atualiza o
# repositório na mão sem publicar faria o script achar que não há trabalho.
if [ "$PUBLICADO" = "$NOVO" ] && [ -f "$DESTINO/index.html" ] && [ "${1:-}" != "--forcar" ]; then
  echo "nada a publicar — $(git log --oneline -1 origin/main)"
  exit 0
fi

echo "==> Atualizando o repositório"
git checkout --quiet main
git reset --quiet --hard origin/main
echo "    $(git log --oneline -1)"

echo "==> Regerando as páginas"
python3 build/build.py > /dev/null

echo "==> Sincronizando para $DESTINO"
mkdir -p "$DESTINO"
rsync -a --delete \
  --include='index.html' --include='404.html' --include='og.png' \
  --include='robots.txt' --include='sitemap.xml' \
  --include='assets/***' \
  --include='calculadora/***' \
  --include='grama-decorativa/***' \
  --include='grama-playground/***' \
  --include='grama-alto-trafego/***' \
  --include='projetos/***' \
  --include='perguntas-frequentes/***' \
  --include='politica-de-privacidade/***' \
  --exclude='*' \
  "$REPO"/ "$DESTINO"/

# A marca fica fora da raiz web: o rsync --delete apagaria um arquivo
# solto dentro de $DESTINO, e não há razão para servi-la.
mkdir -p "$ESTADO"
echo "$NOVO" > "$MARCA"

echo "==> Pronto: $(find "$DESTINO" -type f | wc -l) arquivos publicados em $(git log --oneline -1 --format=%h)"
exit 0
}
