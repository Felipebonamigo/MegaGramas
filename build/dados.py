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
PRECO_MINIMO = "19,90"

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
      r="A melhor altura depende do uso e do visual desejado. As linhas de 10 e 12 mm têm fibras mais baixas e acabamento compacto. As de 20 mm oferecem um visual mais preenchido. As linhas Natural Garden, de 20 e 32 mm, combinam dois tons de verde e fibras marrons para imitar um gramado natural. A Mega Gramas ajuda você a escolher a linha mais adequada para o seu espaço."),
 dict(g="escolha", top=False, p="Qual a diferença entre gramas de diferentes alturas?",
      r="A diferença está no comprimento dos fios, que influencia o visual e a sensação ao toque. Fibras mais baixas (10 e 12 mm) dão acabamento compacto e uniforme; as de 20 mm têm aspecto mais preenchido; e a Natural Garden+ de 32 mm é a mais volumosa e a que mais se aproxima de um gramado natural. Além da altura, a cor e a linha também fazem diferença na escolha do modelo ideal para seu espaço."),
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
      r="Sim! A grama sintética é vendida por metro quadrado inteiro, com venda mínima de 1 m². Os rolos têm 2 metros de largura e 25 metros de comprimento (50 m²), e cortamos na metragem que você precisa. Como a largura é fixa, a quantidade a comprar pode ser maior que a área do espaço: o material é cortado em faixas de 2 metros, e isso gera sobras e emendas. A calculadora do site faz essa estimativa para você."),
 dict(g="compra", top=False, p="Vocês fazem cortes sob medida?",
      r="Sim. O rolo tem 2 metros de largura e a venda é por m² inteiro, então cortamos o comprimento na metragem necessária. Dependendo do formato do espaço, o projeto pode exigir recortes e emendas. Envie as medidas para confirmarmos as opções de corte do modelo escolhido."),
 dict(g="compra", top=False, p="Vocês fazem instalação?",
      r="Sim! A Mega Gramas realiza a instalação, principalmente em Porto Alegre e na Região Metropolitana. Também atendemos outras cidades, com adicional de deslocamento. Entre em contato e informe sua localização e as medidas do espaço para consultar a disponibilidade e solicitar um orçamento."),
 dict(g="compra", top=False, p="Vocês entregam em quais regiões?",
      r="Entregamos grama sintética para todo o Brasil! O frete e o prazo de entrega são calculados conforme o CEP e o tamanho do pedido. Já o serviço de instalação é realizado nos estados do Rio Grande do Sul e Santa Catarina, mediante consulta de disponibilidade e valor de deslocamento."),
 dict(g="compra", top=True, p="Existe garantia?",
      r="Sim! A garantia varia de 3 a 12 meses, conforme o modelo escolhido, e cobre defeitos de fabricação. Ela não cobre danos causados por mau uso, instalação inadequada ou limpeza com produtos que danifiquem a grama. Consulte com a nossa equipe o prazo do modelo que você escolheu."),
 dict(g="compra", top=True, p="Como calculo quantos metros preciso?",
      r="Multiplique a largura pelo comprimento do espaço. Por exemplo: 3 metros de largura por 4 metros de comprimento dão 12 m². Só que o rolo tem 2 metros de largura fixa, então a quantidade a comprar considera as faixas inteiras, os recortes e as emendas — um espaço de 7,5 m × 7 m tem 52,5 m², mas exige 56 m² de grama. Use a calculadora do site ou envie as medidas para a Mega Gramas."),
]

# Catálogo comercial vigente (nov/2026), conforme o documento enviado pelo
# cliente: nomes, alturas e ordem são os oficiais. Não entram garantia,
# preço individual nem especificação técnica não confirmada (UV, drenagem,
# durabilidade). O preço inicial da linha, R$ 19,90, aparece numa chamada só.
#
# foto=None => o card mostra a amostra de cor da linha, sem foto. Hoje só há
# fotos de fibra para três alturas (12, 20 e 30 mm); as demais linhas esperam
# fotos do cliente.
MODELOS = [
 dict(
  slug="mega-economica-10mm", nome="Mega Econômica 10mm", altura="10mm",
  linha="Linha Econômica", indicacao="Ambientes internos e áreas externas cobertas",
  foto=None, cores=["#3F9A2E"],
  texto=["A Mega Econômica 10mm é uma linha de grama sintética desenvolvida para quem busca uma solução prática, econômica e acessível para renovar ambientes.",
         "Com fibras verdes de 10mm de altura e perfil baixo e compacto, é uma excelente opção para projetos decorativos."],
  specs=[("Altura das fibras", "10mm"), ("Cor", "Verde"), ("Categoria", "Linha Econômica"),
         ("Indicação", "Ambientes internos e áreas externas cobertas")],
  aplicacoes=["Lojas", "Vitrines", "Eventos", "Espaços decorativos"],
  diferenciais=["Economia", "Praticidade", "Perfil compacto"],
  fecho="Mega Econômica 10mm — Renove seus ambientes com economia."),
 dict(
  slug="mega-decor-12mm", nome="Mega Decor 12mm", altura="12mm",
  linha="Linha Decorativa", indicacao="Ambientes internos e áreas externas cobertas",
  foto=None, cores=["#43A02E"],
  texto=["A Mega Decor 12mm é uma linha de grama sintética decorativa, ideal para quem deseja transformar ambientes de forma simples, prática e econômica.",
         "Com fibras de 12mm de altura e coloração verde, proporciona um visual agradável e um toque de natureza aos espaços, valorizando a decoração de ambientes residenciais e comerciais.",
         "Versátil e funcional, é indicada para ambientes internos, sacadas e varandas cobertas, vitrines, eventos, cenários e espaços decorativos."],
  specs=[("Altura das fibras", "12mm"), ("Cor", "Verde"), ("Categoria", "Linha Decorativa"),
         ("Indicação", "Ambientes internos e áreas externas cobertas")],
  aplicacoes=["Residências", "Lojas", "Vitrines", "Eventos", "Cenários", "Sacadas e varandas cobertas"],
  diferenciais=["Versatilidade", "Praticidade", "Excelente custo-benefício"],
  fecho="Mega Decor 12mm — Praticidade e beleza para sua decoração."),
 dict(
  slug="mega-plus-12mm", nome="Mega Plus 12mm", altura="12mm",
  linha="Linha Versátil", indicacao="Ambientes internos e externos",
  foto="fibra-12mm", cores=["#4CAA33"],
  texto=["A Mega Plus 12mm é uma linha de grama sintética que combina beleza, praticidade e versatilidade para diferentes ambientes.",
         "Desenvolvida para quem prefere gramas com fibras mais baixas, oferece um visual uniforme e um acabamento elegante, sendo uma excelente escolha para valorizar espaços residenciais e comerciais.",
         "Ideal para jardins, quintais, varandas, áreas de lazer e bordas de piscinas, proporciona um toque de verde aos ambientes, unindo estética e funcionalidade."],
  specs=[("Altura das fibras", "12mm"), ("Cor", "Verde"), ("Categoria", "Linha Versátil"),
         ("Indicação", "Ambientes internos e externos")],
  aplicacoes=["Jardins", "Quintais", "Varandas", "Áreas de lazer", "Bordas de piscinas"],
  diferenciais=["Perfil baixo", "Visual uniforme", "Versatilidade", "Acabamento diferenciado"],
  fecho="Mega Plus 12mm — Mais versatilidade para transformar seus espaços."),
 dict(
  slug="mega-plus-mais-20mm", nome="Mega Plus+ 20mm", altura="20mm",
  linha="Linha Versátil", indicacao="Ambientes internos e externos",
  foto="fibra-20mm", cores=["#4CAA33"],
  texto=["A Mega Plus+ 20mm é uma linha de grama sintética que combina beleza, praticidade e versatilidade, oferecendo fibras mais altas para quem busca um visual mais volumoso e um acabamento diferenciado.",
         "Com fios de 20mm de altura, mantém a proposta versátil da Mega Plus 12mm, proporcionando um aspecto mais preenchido e agradável aos ambientes.",
         "Ideal para jardins, quintais, varandas, áreas de lazer e bordas de piscinas, é uma excelente escolha para valorizar espaços residenciais e comerciais."],
  specs=[("Altura das fibras", "20mm"), ("Cor", "Verde"), ("Categoria", "Linha Versátil"),
         ("Indicação", "Ambientes internos e externos")],
  aplicacoes=["Jardins", "Quintais", "Varandas", "Áreas de lazer", "Bordas de piscinas"],
  diferenciais=["Fibras mais altas", "Maior volume visual", "Versatilidade", "Acabamento diferenciado"],
  fecho="Mega Plus+ 20mm — Mais volume e beleza para seus ambientes."),
 dict(
  slug="mega-natural-garden-20mm", nome="Mega Natural Garden 20mm", altura="20mm",
  linha="Linha Natural", indicacao="Ambientes internos e externos",
  foto=None, cores=["#3C8F2B", "#6DBF3E", "#A98B5B"],
  texto=["A Mega Natural Garden 20mm é uma linha de grama sintética que combina beleza, sofisticação e naturalidade, proporcionando um visual realista para diferentes ambientes.",
         "Com fibras de 20mm de altura, apresenta uma combinação de dois tons de verde e fibras marrons que simulam a grama natural seca, criando um efeito mais autêntico e um acabamento diferenciado.",
         "Ideal para jardins, quintais, varandas, áreas de lazer e bordas de piscinas, é uma excelente escolha para quem deseja transformar espaços com a beleza da grama natural e a praticidade da grama sintética."],
  specs=[("Altura das fibras", "20mm"), ("Cor", "Dois tons de verde + marrom"), ("Categoria", "Linha Natural"),
         ("Indicação", "Ambientes internos e externos")],
  aplicacoes=["Jardins", "Quintais", "Varandas", "Áreas de lazer", "Bordas de piscinas"],
  diferenciais=["Aparência realista", "Combinação de três tonalidades", "Volume visual", "Acabamento natural"],
  fecho="Mega Natural Garden 20mm — A beleza da natureza em cada detalhe."),
 dict(
  slug="mega-natural-garden-mais-32mm", nome="Mega Natural Garden+ 32mm", altura="32mm",
  linha="Linha Natural", indicacao="Ambientes internos e externos",
  foto="fibra-real30", cores=["#3C8F2B", "#6DBF3E", "#A98B5B"],
  texto=["A Mega Natural Garden+ 32mm é uma linha de grama sintética que combina beleza, sofisticação e naturalidade, proporcionando um visual ainda mais volumoso e realista para diferentes ambientes.",
         "Com fibras de 32mm de altura, oferece um aspecto mais cheio e exuberante, valorizando os espaços com um acabamento elegante e uma aparência próxima à grama natural.",
         "Ideal para jardins, quintais, varandas, áreas de lazer e projetos paisagísticos, é uma excelente escolha para quem busca um visual mais encorpado, unindo a beleza da natureza à praticidade da grama sintética."],
  specs=[("Altura das fibras", "32mm"), ("Categoria", "Linha Natural"),
         ("Indicação", "Ambientes internos e externos")],
  aplicacoes=["Jardins", "Quintais", "Varandas", "Áreas de lazer", "Projetos paisagísticos"],
  diferenciais=["Fibras mais altas", "Maior volume visual", "Aparência realista", "Acabamento natural"],
  fecho="Mega Natural Garden+ 32mm — Mais volume, mais naturalidade e beleza para seus espaços."),
 dict(
  slug="mega-color-12mm", nome="Mega Color 12mm", altura="12mm",
  linha="Linha Colorida", indicacao="Ambientes decorativos e projetos personalizados",
  foto=None, cores=["#1F5FBF", "#1A1A1A", "#C62828"], cores_nomes="Azul, preto e vermelho",
  texto=["A Mega Color 12mm é uma linha de grama sintética desenvolvida para quem busca criatividade, estilo e personalidade na decoração de diferentes ambientes.",
         "Com fibras de 12mm de altura, está disponível nas cores azul, preto e vermelho, oferecendo diversas possibilidades para transformar espaços com um visual moderno, marcante e diferenciado.",
         "Ideal para ambientes comerciais, vitrines, eventos, cenários, espaços recreativos e projetos decorativos, é uma excelente escolha para quem deseja sair do tradicional e criar ambientes únicos e personalizados."],
  specs=[("Altura das fibras", "12mm"), ("Cores disponíveis", "Azul, preto e vermelho"), ("Categoria", "Linha Colorida"),
         ("Indicação", "Ambientes decorativos e projetos personalizados")],
  aplicacoes=["Lojas", "Vitrines", "Eventos", "Cenários", "Espaços recreativos", "Ambientes comerciais"],
  diferenciais=["Variedade de cores", "Versatilidade decorativa", "Visual moderno", "Acabamento diferenciado"],
  fecho="Mega Color 12mm — Mais cores, criatividade e personalidade para seus espaços."),
]

# Rolo: 2 m de largura e 25 m de comprimento (50 m²) em todos os modelos.
# A venda é por m² inteiro, mínimo 1 m² (informado pelo cliente em nov/2026).
ROLO_LARGURA = 2
ROLO_COMPRIMENTO = 25

# Linha de colas de contato Quimicolla, revendida pela Mega Gramas, com
# autorização do cliente para usar nome e marca. Rendimentos são estimativas
# informadas pelo cliente. Sem preço, de propósito: o valor sai pelo WhatsApp.
COLAS = [
  dict(nome="Quimicolla 700 g", rendimento="3 a 5 m²"),
  dict(nome="Quimicolla 2,8 kg", rendimento="20 a 30 m²"),
  dict(nome="Quimicolla 14 kg", rendimento="60 a 100 m²"),
]

# Depoimentos reais entram aqui quando existirem; a seção os mostra
# automaticamente e deixa de mostrar o bloco institucional. Cada item:
#   dict(texto="…", nome="Nome S.", cidade="Cidade/UF", projeto="Residencial")
# Só com autorização de quem falou. Nota de avaliação: só se for medida.
DEPOIMENTOS = []

NUMERO_CLIENTES = "+500"   # "mais de 500 clientes satisfeitos", confirmado pelo cliente

INSTITUCIONAL = [
  ("Atendimento personalizado", "Cada projeto começa pelas medidas e pelo uso do seu espaço."),
  ("Orientação na escolha", "Ajuda para decidir a altura e a linha de grama mais adequadas."),
  ("Cálculo da quantidade", "Auxílio para estimar quanto comprar, sem faltar nem sobrar demais."),
  ("Qualidade dos produtos", "Linhas selecionadas para cada tipo de ambiente."),
  ("Compromisso com o cliente", "Acompanhamos o projeto até a satisfação de quem compra."),
]

# Cards de "onde utilizar": só entram os que têm foto, nomeada em assets/fotos/.
APLICACOES_HOME = [
  dict(nome="Jardins e residências",        foto="amb-jardim",     legenda="Jardim residencial com grama sintética"),
  dict(nome="Áreas de lazer e piscina",     foto="amb-piscina",    legenda="Área de piscina com grama sintética"),
  dict(nome="Playgrounds e escolas",        foto="amb-playground", legenda="Playground com grama sintética"),
  dict(nome="Academias e áreas de treino",  foto="amb-academia",   legenda="Academia com grama sintética na área funcional"),
]

# Atendidos, mas sem foto: entram como uma linha de texto no fim da seção.
APLICACOES_TEXTO = ("Também atendemos sacadas e varandas, áreas comuns de condomínio, "
                    "empresas e escritórios e a circulação no entorno de quadras.")

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
  dict(arq="ad-piscina-gramado", titulo="Piscina com gramado",
       desc="O gramado natural ao redor da piscina deu lugar à grama sintética."),
  dict(arq="ad-piscina-deck", titulo="Deck de piscina",
       desc="O piso de pedra ao redor da piscina foi coberto por grama."),
  dict(arq="ad-piscina-brita", titulo="Piscina em área estreita",
       desc="A brita deu lugar à grama em volta da piscina."),
  dict(arq="ad-playground-areia", titulo="Playground com areia",
       desc="A areia do entorno dos brinquedos deu lugar à grama."),
  dict(arq="ad-playground-concreto", titulo="Playground em terraço",
       desc="O piso de concreto deu lugar à grama sob os brinquedos."),
  dict(arq="ad-predio-gramado", titulo="Área externa de prédio",
       desc="O piso cinza junto ao edifício ganhou um gramado."),
  dict(arq="ad-entrada-pedra", titulo="Entrada com piso de pedra",
       desc="Faixas de grama sobre o piso de pedra da entrada."),
  dict(arq="ad-patio-externo", titulo="Pátio externo",
       desc="O piso de concreto deu lugar à grama."),
]
