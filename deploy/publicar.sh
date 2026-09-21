#!/usr/bin/env bash
# Publica o site no VPS. Rodar NO SERVIDOR:
#
#   bash /opt/megagramas/deploy/publicar.sh
#
# Busca a última versão do repositório, regera as páginas e sincroniza
# apenas os arquivos públicos para /var/www/megagramas.
set -euo pipefail

REPO="${REPO:-/opt/megagramas}"
DESTINO="${DESTINO:-/var/www/megagramas}"

cd "$REPO"
echo "==> Buscando a última versão"
git fetch --quiet origin main
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

chown -R www-data:www-data "$DESTINO" 2>/dev/null || true
echo "==> Pronto: $(find "$DESTINO" -type f | wc -l) arquivos em $DESTINO"
