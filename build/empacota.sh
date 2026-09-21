#!/usr/bin/env bash
# Gera o pacote para subir na hospedagem.
#
#   bash build/empacota.sh
#
# Produz megagramas-site.zip com apenas o que vai para o servidor — fica de
# fora o gerador, o CI e a documentação, que não têm por que estar num site
# público.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 build/build.py >/dev/null
echo "páginas regeradas"

SAIDA="megagramas-site.zip"
rm -f "$SAIDA"

zip -rq "$SAIDA" \
  index.html 404.html .htaccess og.png robots.txt sitemap.xml \
  assets \
  calculadora grama-decorativa grama-playground grama-alto-trafego \
  projetos perguntas-frequentes politica-de-privacidade \
  -x '*.DS_Store'

echo "$SAIDA: $(du -h "$SAIDA" | cut -f1), $(unzip -l "$SAIDA" | tail -1 | awk '{print $2}') arquivos"
