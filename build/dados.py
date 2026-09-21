# -*- coding: utf-8 -*-
"""Conteúdo do site. Editar aqui e rodar `python3 build/build.py`."""

SITE = "https://megagramas.com.br"
MARCA = "MegaGramas"
SLOGAN = "Naturalmente mais possibilidades"
ANOS = 12

# Navegação principal. Caminhos relativos à raiz; o build resolve por página.
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

# top=True aparece também na home, nas perguntas que mais travam a compra.
PERGUNTAS = [
 dict(g="escolha", top=True, p="Qual a melhor altura de grama sintética?",
      r="Não existe uma altura melhor — existe a adequada para o uso. Fibras mais baixas (12 a 20 mm) são mais firmes e se comportam melhor em circulação intensa. Fibras mais altas (25 a 40 mm) são mais macias e volumosas, indicadas para lazer, playground e áreas de estar. Na dúvida, descreva o espaço e o uso que a equipe indica."),
 dict(g="escolha", top=False, p="Qual a diferença entre gramas de diferentes alturas?",
      r="Altura maior significa mais maciez e volume visual, indicada para lazer e decoração. Altura menor significa fibra mais firme, que se recupera melhor em áreas de circulação intensa."),
 dict(g="instalacao", top=True, p="Pode instalar sobre cimento?",
      r="Sim, é uma das bases mais comuns. A superfície precisa estar limpa, seca e nivelada, e o local deve ter caimento para o escoamento da água. Dependendo do caso, usa-se manta sob a grama."),
 dict(g="instalacao", top=False, p="Pode instalar diretamente sobre terra?",
      r="Sim, desde que o solo seja nivelado e compactado. O ideal é preparar uma base (pó de pedra ou areia) e aplicar manta antiervas por baixo, para evitar o crescimento de mato através da grama."),
 dict(g="instalacao", top=True, p="A água da chuva escoa?",
      r="Sim. A base da grama é perfurada com furos de drenagem. O escoamento depende também da base: sobre cimento, é preciso haver caimento; sobre terra, o solo precisa drenar."),
 dict(g="uso", top=True, p="A grama sintética esquenta no sol?",
      r="Sim. Em exposição direta ela esquenta mais que a grama natural, principalmente nos horários de sol forte. Molhar a superfície antes de usar reduz a sensação de calor na hora, e áreas com alguma sombra são mais confortáveis. Vale considerar isso ao escolher o local de aplicação."),
 dict(g="uso", top=False, p="Pode molhar?",
      r="Pode. Chuva, mangueira e lavagem não são problema — a drenagem existe justamente para isso."),
 dict(g="uso", top=True, p="Pode ser usada em ambientes com animais?",
      r="Sim, é uma aplicação comum. A limpeza é feita com água e, quando necessário, sabão neutro. A drenagem facilita a higienização."),
 dict(g="uso", top=True, p="Qual a durabilidade?",
      r="Varia conforme o modelo, a intensidade de uso, a exposição ao sol e a manutenção. Os modelos que trabalhamos têm proteção UV, e a garantia é de 3 ou 12 meses conforme a linha — indicada em cada produto."),
 dict(g="uso", top=False, p="Como fazer a limpeza?",
      r="Varrer ou rastelar folhas e sujeira seca, aspirar quando necessário e lavar com água. Manchas saem com água e sabão neutro. Rastelar as fibras de vez em quando ajuda a manter o aspecto."),
 dict(g="compra", top=True, p="É vendida por m²?",
      r="O rolo tem 2,00 m de largura fixa e é vendido por metro linear — cada metro linear equivale a 2 m². Por isso o cálculo é feito em faixas de 2 m e não apenas pela área do espaço. A calculadora do site faz essa conta."),
 dict(g="compra", top=False, p="Vocês fazem cortes sob medida?",
      r="Sim, conforme a necessidade do projeto e a disponibilidade do modelo escolhido."),
 dict(g="compra", top=False, p="Vocês fazem instalação?",
      r="Sim, conforme a região. Também atendemos quem quer apenas o material, na medida necessária."),
 dict(g="compra", top=False, p="Vocês entregam em quais regiões?",
      r="Entregamos o material para todo o Brasil. O serviço de instalação é oferecido conforme a disponibilidade regional — consulte a sua cidade pelo WhatsApp."),
 dict(g="compra", top=True, p="Existe garantia?",
      r="Sim. Os modelos têm garantia de 3 ou 12 meses, conforme a linha. A garantia aplicável está indicada em cada produto."),
 dict(g="compra", top=False, p="Como calculo quantos metros preciso?",
      r="Use a calculadora do site: informe largura e comprimento e ela monta as faixas de 2 m, mostra as emendas e a sobra de corte. Se o espaço for irregular, envie as medidas e uma foto que a equipe calcula para você."),
]

MODELOS = [
 dict(
  slug="grama-decorativa", nome="Decorativa", altura="12 a 25 mm",
  titulo="Grama Sintética Decorativa 12 a 25 mm",
  desc="Grama sintética decorativa para jardins, varandas, fachadas e ambientes residenciais. Venda por metro linear, corte sob medida e orientação para escolher a altura.",
  h1="Grama sintética decorativa",
  intro="A linha decorativa existe para resolver aparência. É a escolha quando o espaço é para ser olhado mais do que pisado: jardim que não vinga na sombra, varanda de apartamento, fachada, parede verde, canteiro que vive falhado.",
  specs=[("Altura", "12 a 25 mm"), ("Maciez", "Média"), ("Resistência", "Uso leve a moderado"),
         ("Fibra", "Acabamento uniforme, tons variados"), ("Proteção", "UV"), ("Uso", "Interno e externo")],
  aplicacoes=["Jardins residenciais", "Sacadas e varandas", "Fachadas e paredes verdes",
              "Recepções e vitrines", "Canteiros e floreiras", "Áreas de circulação leve"],
  alturas=[("12 mm", "Fachadas, paredes verdes e circulação leve. Fibra baixa e firme, acabamento mais discreto."),
           ("20 mm", "Meio-termo mais pedido. Varandas, jardins pequenos e áreas de apoio."),
           ("25 mm", "Jardim residencial com uso de estar. Mais volume e sensação de gramado.")],
  aviso="Em fachada e parede verde a exposição ao sol é constante e direta. A proteção UV é o que segura a cor ao longo do tempo — confirme com a equipe o modelo indicado para aplicação vertical.",
  foto="Jardim residencial finalizado, luz do dia"),
 dict(
  slug="grama-playground", nome="Lazer e Playground", altura="25 a 40 mm",
  titulo="Grama Sintética para Playground e Lazer 25 a 40 mm",
  desc="Grama sintética para playground, escolas, condomínios e áreas de lazer. Fibra alta e macia, corte sob medida e instalação conforme a região.",
  h1="Grama sintética para lazer e playground",
  intro="Aqui o critério é o toque. São espaços onde criança senta, deita e cai — e onde adulto anda descalço. A fibra é mais alta e mais macia, e o preenchimento é maior para o pisoteio não deixar marca permanente.",
  specs=[("Altura", "25 a 40 mm"), ("Maciez", "Alta"), ("Resistência", "Uso recreativo frequente"),
         ("Fibra", "Alta densidade, toque macio"), ("Proteção", "UV"), ("Uso", "Interno e externo")],
  aplicacoes=["Playgrounds", "Escolas e creches", "Áreas de lazer de condomínio",
              "Espaço pet", "Áreas gourmet e piscina", "Salões de festa infantil"],
  alturas=[("25 mm", "Áreas de lazer adulto, entorno de piscina e espaço gourmet."),
           ("32 mm", "A mais usada em playground e área de lazer de condomínio."),
           ("40 mm", "Máximo de maciez e volume. Espaços infantis e áreas de estar no chão.")],
  aviso="Grama sintética dá conforto ao toque, mas não é piso de amortecimento de impacto. Quando houver brinquedo com altura de queda, a base sob a grama é que precisa resolver a segurança — fale com a equipe antes de definir o projeto.",
  foto="Playground finalizado com brinquedos"),
 dict(
  slug="grama-alto-trafego", nome="Alto Tráfego", altura="12 a 20 mm",
  titulo="Grama Sintética para Alto Tráfego 12 a 20 mm",
  desc="Grama sintética para áreas comerciais, condomínios e circulação intensa. Fibra firme de 12 a 20 mm, venda por metro linear e corte sob medida.",
  h1="Grama sintética para alto tráfego",
  intro="Fibra baixa e firme, feita para lugar onde passa gente o dia inteiro. Fibra alta em corredor comercial deita em duas semanas e não levanta mais — é o erro mais comum e o mais caro de corrigir.",
  specs=[("Altura", "12 a 20 mm"), ("Maciez", "Baixa — fibra firme"), ("Resistência", "Circulação intensa"),
         ("Fibra", "Baixa e densa, boa recuperação"), ("Proteção", "UV"), ("Uso", "Interno e externo")],
  aplicacoes=["Corredores e recepções comerciais", "Áreas comuns de condomínio",
              "Circulação em escolas", "Entorno de quadras esportivas",
              "Estandes, feiras e eventos", "Calçadas e passagens"],
  alturas=[("12 mm", "Circulação mais pesada. A fibra mais firme da linha, com a melhor recuperação."),
           ("15 mm", "Comércio e condomínio com fluxo constante e alguma exigência visual."),
           ("20 mm", "Circulação moderada, quando o visual pesa mais que o fluxo.")],
  aviso="No entorno de quadras a grama resolve circulação e acabamento, não a prática esportiva. Campo e quadra de jogo pedem grama esportiva, que não faz parte do nosso catálogo.",
  foto="Corredor comercial ou área comum de condomínio"),
]

APLICACOES_HOME = ["Jardins e residências", "Sacadas e varandas", "Condomínios",
                   "Empresas e escritórios", "Playgrounds e escolas", "Áreas de lazer",
                   "Circulação em áreas esportivas"]
