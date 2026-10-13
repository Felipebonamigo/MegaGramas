# -*- coding: utf-8 -*-
"""Conteúdo do site. Editar aqui e rodar `python3 build/build.py`."""

SITE = "https://megagramas.com.br"
MARCA = "Mega Gramas"
SLOGAN = "Naturalmente mais possibilidades"
ANOS = 12

RAZAO_SOCIAL = "MAURICIO GOULART CORREA - ME"
NOME_FANTASIA = "CAMA ELÁSTICA RS"
CNPJ = "07.078.441/0001-55"
EMAIL = "megagramas@gmail.com"
WHATSAPP_EXIBIDO = "(51) 99969-4547"
PRECO_MINIMO = "24,20"

NAV = [
    ("Modelos", "index.html#modelos"),
    ("Calculadora", "calculadora/index.html"),
    ("Projetos", "projetos/index.html"),
    ("Dúvidas", "perguntas-frequentes/index.html"),
]

GRUPOS_FAQ = [
    ("escolha", "Escolher o modelo"),
    ("instalacao", "Instalação e base"),
    ("uso", "Uso, limpeza e durabilidade"),
    ("compra", "Compra, entrega e garantia"),
]

# Respostas revisadas e aprovadas pelo cliente (FAQ_RESPOSTAS.docx).
# top=True aparece também na home, nas perguntas que mais travam a compra.
PERGUNTAS = [
 dict(g="escolha", top=True, p="Qual a melhor altura de grama sintética?",
      r="A melhor altura depende do uso e do visual desejado. A grama de 12 mm oferece um acabamento mais baixo e compacto. A de 20 mm é uma opção intermediária. Já o modelo Real de 30 mm, com dois tons de verde e fios cor de palha, é ideal para quem busca a aparência de um gramado natural. A Mega Gramas ajuda você a escolher o modelo mais adequado para o seu espaço."),
 dict(g="escolha", top=False, p="Qual a diferença entre gramas de diferentes alturas?",
      r="A diferença está no comprimento dos fios, que influencia o visual e a sensação ao toque. A 12 mm tem acabamento mais baixo e compacto; a 20 mm oferece fios mais altos; e a Real de 30 mm combina dois tons de verde e fios cor de palha para imitar um gramado natural. Além da altura, o tipo de fio e a densidade também fazem diferença na escolha do modelo ideal para seu espaço."),
 dict(g="instalacao", top=True, p="Pode instalar sobre cimento?",
      r="Sim! A grama sintética pode ser instalada sobre cimento ou concreto, desde que a superfície esteja firme, limpa, seca e sem irregularidades importantes. Em áreas externas, é essencial garantir o escoamento da água para evitar poças sob a grama."),
 dict(g="instalacao", top=False, p="Pode instalar diretamente sobre terra?",
      r="Sim, mas a terra precisa ser preparada antes da instalação. É necessário retirar a vegetação, nivelar e compactar o solo, além de preparar uma base adequada para a drenagem. Esse cuidado ajuda a evitar afundamentos, irregularidades e acúmulo de água."),
 dict(g="instalacao", top=True, p="A água da chuva escoa?",
      r="Sim! A grama sintética com base perfurada permite a passagem da água da chuva. Para que ela escoe corretamente, o piso ou solo também precisa ter uma drenagem adequada. Sobre cimento, é necessário manter o caimento e as saídas de água livres para evitar poças."),
 dict(g="uso", top=True, p="A grama sintética esquenta no sol?",
      r="Sim. Sob sol forte, a grama sintética pode ficar quente, especialmente em dias de calor intenso. Em áreas usadas por crianças e pets, recomendamos conferir a temperatura antes do contato e priorizar espaços com sombra."),
 dict(g="uso", top=False, p="Pode molhar?",
      r="Sim! A grama sintética pode molhar com chuva ou durante a limpeza. O importante é que a instalação tenha drenagem adequada para evitar água acumulada. Após a instalação, respeite o tempo de secagem da cola antes de molhar o local."),
 dict(g="uso", top=True, p="Pode ser usada em ambientes com animais?",
      r="Sim! A grama sintética pode ser usada em espaços com animais. Para manter o ambiente limpo, recolha os resíduos sólidos e lave o local regularmente com água e sabão neutro, enxaguando bem. Uma boa drenagem ajuda a evitar acúmulo de urina e odores. Em áreas ao sol, confira a temperatura da grama antes de liberar o acesso dos pets."),
 dict(g="uso", top=True, p="Qual a durabilidade?",
      r="A durabilidade varia conforme o modelo, a intensidade de uso, a exposição ao sol e os cuidados com a limpeza. Uma instalação bem feita e a manutenção adequada ajudam a conservar a grama por mais tempo. A Mega Gramas orienta você sobre a vida útil esperada para o modelo escolhido e seu local de instalação."),
 dict(g="uso", top=False, p="Como fazer a limpeza?",
      r="Retire folhas e resíduos com uma vassoura de cerdas macias. Quando necessário, lave com água e sabão neutro, enxaguando bem. Evite escovas de aço, solventes e produtos abrasivos, que podem danificar os fios e a base da grama."),
 dict(g="compra", top=True, p="É vendida por m²?",
      r="Sim! A grama sintética é vendida por metro quadrado (m²). Para calcular a área, multiplique a largura pelo comprimento do espaço. A quantidade necessária pode incluir uma margem para recortes e emendas, conforme o formato do local."),
 dict(g="compra", top=False, p="Vocês fazem cortes sob medida?",
      r="Envie as medidas do seu espaço para consultarmos as opções de corte disponíveis. O corte depende da largura do rolo e do modelo escolhido, podendo exigir recortes e emendas na instalação."),
 dict(g="compra", top=False, p="Vocês fazem instalação?",
      r="Sim! A Mega Gramas realiza a instalação, principalmente em Porto Alegre e na Região Metropolitana. Também atendemos outras cidades, com adicional de deslocamento. Entre em contato e informe sua localização e as medidas do espaço para consultar a disponibilidade e solicitar um orçamento."),
 dict(g="compra", top=False, p="Vocês entregam em quais regiões?",
      r="Entregamos grama sintética para todo o Brasil! O frete e o prazo de entrega são calculados conforme o CEP e o tamanho do pedido. Já o serviço de instalação é realizado nos estados do Rio Grande do Sul e Santa Catarina, mediante consulta de disponibilidade e valor de deslocamento."),
 dict(g="compra", top=True, p="Existe garantia?",
      r="Sim! O modelo de 12 mm possui garantia de 3 meses, e os demais modelos têm garantia de 12 meses contra defeitos de fabricação. A garantia não cobre danos causados por mau uso, instalação inadequada ou limpeza com produtos que danifiquem a grama."),
 dict(g="compra", top=True, p="Como calculo quantos metros preciso?",
      r="Multiplique a largura pelo comprimento do espaço. Por exemplo: uma área de 3 metros de largura por 4 metros de comprimento tem 12 m². Se o local tiver um formato irregular, divida-o em partes e some as áreas. Envie as medidas para a Mega Gramas: ajudamos a calcular a quantidade necessária, considerando a largura do rolo, os recortes e as emendas."),
]

# O catálogo real: três alturas, não três "linhas" por aplicação.
MODELOS = [
 dict(
  slug="grama-12mm", nome="12 mm", altura="12 mm", garantia="3 meses", foto="fibra-12mm",
  titulo="Grama Sintética 12 mm",
  desc=f"Grama sintética de 12 mm, com acabamento baixo e compacto. Indicada para áreas de circulação, comércio e espaços que pedem um visual discreto. A partir de R$ {PRECO_MINIMO} o m².",
  h1="Grama sintética 12 mm",
  intro="Acabamento baixo e compacto. É a altura que resolve circulação: corredor, área comum, estande, entorno de quadra — lugar onde passa gente o dia inteiro e a fibra precisa levantar de novo.",
  specs=[("Altura do fio", "12 mm"), ("Acabamento", "Baixo e compacto"),
         ("Garantia", "3 meses contra defeitos de fabricação"), ("Uso", "Interno e externo")],
  aplicacoes=["Corredores e áreas de circulação", "Áreas comuns de condomínio",
              "Comércio, estandes e eventos", "Entorno de quadras esportivas",
              "Academias e áreas de treino", "Espaços que pedem visual discreto"],
  nota="É o único modelo com garantia de 3 meses; os demais têm 12 meses. A escolha costuma ser essa quando o critério é circulação e custo, e não maciez."),
 dict(
  slug="grama-20mm", nome="20 mm", altura="20 mm", garantia="12 meses", foto="fibra-20mm",
  titulo="Grama Sintética 20 mm",
  desc=f"Grama sintética de 20 mm, o meio-termo entre acabamento e maciez. Indicada para jardins, varandas, playgrounds e áreas de lazer. A partir de R$ {PRECO_MINIMO} o m².",
  h1="Grama sintética 20 mm",
  intro="O meio-termo, e o mais pedido. Fios mais altos que a de 12 mm, sem o volume da Real de 30 mm. Funciona bem onde o espaço é para usar e para olhar ao mesmo tempo.",
  specs=[("Altura do fio", "20 mm"), ("Acabamento", "Intermediário"),
         ("Garantia", "12 meses contra defeitos de fabricação"), ("Uso", "Interno e externo")],
  aplicacoes=["Jardins residenciais", "Sacadas e varandas", "Playgrounds e escolas",
              "Áreas de lazer e piscina", "Espaço pet", "Áreas de condomínio"],
  nota="Quando a dúvida é entre 12 mm e Real de 30 mm, costuma ser esta. Em caso de dúvida, peça uma amostra antes de fechar."),
 dict(
  slug="grama-real-30mm", nome="Real 30 mm", altura="30 mm", garantia="12 meses", foto="fibra-real30",
  titulo="Grama Sintética Real 30 mm",
  desc=f"Grama sintética Real de 30 mm, com dois tons de verde e fios cor de palha para imitar um gramado natural. Indicada para jardins e áreas de estar. A partir de R$ {PRECO_MINIMO} o m².",
  h1="Grama sintética Real 30 mm",
  intro="Dois tons de verde e fios cor de palha entre as fibras. É o modelo que imita gramado natural — a palha faz o trabalho que o verde sozinho não faz, porque gramado de verdade nunca é de uma cor só.",
  specs=[("Altura do fio", "30 mm"), ("Acabamento", "Dois tons de verde e fios cor de palha"),
         ("Garantia", "12 meses contra defeitos de fabricação"), ("Uso", "Interno e externo")],
  aplicacoes=["Jardins residenciais", "Áreas de estar e lazer", "Entorno de piscina",
              "Áreas gourmet", "Fachadas e paisagismo", "Espaços de contemplação"],
  nota="É a escolha quando o objetivo é a aparência de gramado natural. Vale ver pessoalmente: a diferença entre ela e a de 20 mm aparece muito mais ao vivo que em foto."),
]

# Cards de "onde utilizar". foto=None ainda usa espaço reservado; quando a
# foto chegar, basta nomear o arquivo exportado em assets/fotos/.
APLICACOES_HOME = [
  dict(nome="Jardins e residências",        foto="amb-jardim",     legenda="Jardim residencial com grama sintética"),
  dict(nome="Áreas de lazer e piscina",     foto="amb-piscina",    legenda="Área de piscina com grama sintética"),
  dict(nome="Playgrounds e escolas",        foto="amb-playground", legenda="Playground com grama sintética"),
  dict(nome="Academias e áreas de treino",  foto="amb-academia",   legenda="Academia com grama sintética na área funcional"),
  dict(nome="Sacadas e varandas",           foto=None, legenda="Varanda de apartamento"),
  dict(nome="Condomínios",                  foto=None, legenda="Área comum de condomínio"),
  dict(nome="Empresas e escritórios",       foto=None, legenda="Recepção ou área externa comercial"),
  dict(nome="Circulação em áreas esportivas", foto=None, legenda="Entorno de quadra, não o campo de jogo"),
]

PRAZOS = [
    ("Porto Alegre e Região Metropolitana",
     "Entrega própria no mesmo dia, mediante disponibilidade, ou em até 2 dias úteis via transportadora."),
    ("Interior do Rio Grande do Sul", "De 1 a 4 dias úteis."),
    ("Santa Catarina", "De 3 a 5 dias úteis."),
    ("Demais regiões", "Consulte o prazo informando seu CEP."),
]


# Pares de antes e depois. As imagens já vêm com os rótulos ANTES/DEPOIS e a
# marca embutidos, então o site não acrescenta rótulo nenhum — só a legenda.
# Para somar um par novo: exportar em assets/fotos/ e acrescentar aqui.
ANTES_DEPOIS = [
  dict(arq="ad-patio-apartamento", titulo="Pátio de apartamento",
       desc="A pedra britada deu lugar a uma área de estar — o espaço passou a ser usado."),
  dict(arq="ad-corredor-padel", titulo="Corredor entre quadras de padel",
       desc="O concreto da circulação recebeu grama. O piso de jogo é outro produto."),
  dict(arq="ad-academia", titulo="Academia",
       desc="O tatame de EVA deu lugar à grama na área de treino funcional."),
  dict(arq="ad-jardim-condominio", titulo="Jardim de condomínio",
       desc="Grama natural falhada por sombra e circulação, substituída por sintética."),
  dict(arq="ad-corredor-escola", titulo="Corredor de escola",
       desc="Pedra portuguesa irregular substituída por grama em toda a passagem."),
]
