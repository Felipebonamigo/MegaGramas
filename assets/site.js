(function(){
  "use strict";

  /* ===== configuração ===== */
  var WHATSAPP = "5551999694547";    /* 55 + DDD 51 + 99969-4547 */
  var SITE = "megagramas.com.br";
  var LARGURA_ROLO = 2;              /* metros — confirmado pelo cliente.
                                        Mudar isto muda todo o cálculo de faixas. */
  var COMPRIMENTO_ROLO = 25;         /* metros: rolo completo = 25 m x 2 m = 50 m² */
  var M2_POR_ROLO = LARGURA_ROLO * COMPRIMENTO_ROLO;
  var PESO_EMENDA = 1.5;             /* quanto uma emenda "custa", em metros lineares equivalentes */
  /* Cola de contato Quimicolla: rendimento estimado em m² por embalagem,
     informado pelo cliente. Sem preço, de propósito. */
  var COLAS = [
    {nome:"Quimicolla 14 kg",  min:60, max:100},
    {nome:"Quimicolla 2,8 kg", min:20, max:30},
    {nome:"Quimicolla 700 g",  min:3,  max:5}
  ];
  var EPS = 1e-9;

  /* ===== utilitários ===== */
  function fmt(n, casas){
    if (casas === undefined) casas = 2;
    return Number(n).toLocaleString("pt-BR", {minimumFractionDigits:casas, maximumFractionDigits:casas});
  }
  function toNum(v){
    var n = parseFloat(String(v).replace(",", "."));
    return isFinite(n) ? n : 0;
  }
  function el(id){ return document.getElementById(id); }

  /* ===== motor de cálculo ===== */
  function montar(larguraACobrir, comprimentoDaFaixa, orientacao){
    var faixas = Math.ceil(larguraACobrir / LARGURA_ROLO - EPS);
    var linear = faixas * comprimentoDaFaixa;
    /* faixa mais longa que o rolo (25 m) precisa de emenda no comprimento também */
    var pedacos = Math.max(1, Math.ceil(comprimentoDaFaixa / COMPRIMENTO_ROLO - EPS));
    var emendas = Math.max(0, faixas - 1) + faixas * (pedacos - 1);
    return {
      faixas: faixas,
      linear: linear,
      emendas: emendas,
      m2: linear * LARGURA_ROLO,
      orientacao: orientacao,
      custo: linear + emendas * PESO_EMENDA
    };
  }

  function planejar(largura, comprimento){
    /* "vertical": as faixas correm no sentido do comprimento
       "horizontal": as faixas correm no sentido da largura */
    var a = montar(largura, comprimento, "vertical");
    var b = montar(comprimento, largura, "horizontal");
    return (a.custo <= b.custo) ? {rec:a, alt:b} : {rec:b, alt:a};
  }

  /* Rolos: de 1 a 50 m² um rolo cortado na metragem; acima, rolos completos
     de 50 m² mais um rolo com o restante. */
  function rolos(m2){
    var completos = Math.floor(m2 / M2_POR_ROLO + EPS);
    var resto = m2 - completos * M2_POR_ROLO;
    var total = completos + (resto > EPS ? 1 : 0);
    var partes = [];
    if (completos > 0){
      partes.push(completos + (completos === 1 ? " rolo completo" : " rolos completos") +
        " de " + M2_POR_ROLO + " m² (" + COMPRIMENTO_ROLO + " m × " + LARGURA_ROLO + " m)");
    }
    if (resto > EPS){
      partes.push("1 rolo de " + fmt(resto, 0) + " m² (" + fmt(resto / LARGURA_ROLO) + " m × " + LARGURA_ROLO + " m)");
    }
    return {total: total, partes: partes};
  }

  /* Combina embalagens de cola para cobrir a área. Entre as combinações que
     cobrem, prefere poucas embalagens sem muita sobra (cada m² de sobra pesa
     1/10 de uma embalagem). Confere com os exemplos do cliente em rendimento
     máximo: 10 m² -> 2 x 700 g; 50 m² -> 2 x 2,8 kg; 100 m² -> 1 x 14 kg;
     120 m² -> 1 x 14 kg + 1 x 2,8 kg. */
  function cola(area, usarMax){
    var y = COLAS.map(function(c){ return usarMax ? c.max : c.min; });
    var base = Math.floor(area / y[0]);
    var melhor = null;
    for (var n14 = base; n14 <= base + 1; n14++){
      for (var n28 = 0; n28 <= 3; n28++){
        for (var n07 = 0; n07 <= 6; n07++){
          var cobre = n14 * y[0] + n28 * y[1] + n07 * y[2];
          if (cobre + EPS < area) continue;
          var pacotes = n14 + n28 + n07;
          var pontos = pacotes + (cobre - area) / 10;
          if (!melhor || pontos < melhor.pontos - EPS) melhor = {n:[n14, n28, n07], cobre: cobre, pontos: pontos};
        }
      }
    }
    var itens = [];
    for (var i = 0; i < 3; i++){
      if (melhor.n[i] > 0) itens.push(melhor.n[i] + " × " + COLAS[i].nome);
    }
    return {texto: itens.join(" + "), cobre: melhor.cobre};
  }

  /* ===== diagrama ===== */
  function diagrama(p, W, L){
    var vert = p.orientacao === "vertical";
    var ocupaW = vert ? p.faixas * LARGURA_ROLO : W;
    var ocupaL = vert ? L : p.faixas * LARGURA_ROLO;
    var S = 288 / Math.max(ocupaW, ocupaL);
    var padE = 32, padT = 28, padD = 10, padB = 8;
    var w = ocupaW * S, h = ocupaL * S;
    var s = [];

    s.push('<svg class="dgm" viewBox="0 0 ' + (w+padE+padD).toFixed(1) + ' ' + (h+padT+padB).toFixed(1) + '" role="img" aria-label="Diagrama: ' + p.faixas + ' faixas de 2 metros cobrindo a área de ' + fmt(W) + ' por ' + fmt(L) + ' metros">');
    s.push('<defs><pattern id="hachura" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line class="hatch" x1="0" y1="0" x2="0" y2="7" stroke-width="2.4"/></pattern></defs>');
    s.push('<g transform="translate(' + padE + ',' + padT + ')">');

    for (var i = 0; i < p.faixas; i++){
      var x = vert ? i * LARGURA_ROLO * S : 0;
      var y = vert ? 0 : i * LARGURA_ROLO * S;
      var fw = vert ? LARGURA_ROLO * S : w;
      var fh = vert ? h : LARGURA_ROLO * S;
      s.push('<rect class="faixa' + (i % 2 ? " alt" : "") + '" x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" width="' + fw.toFixed(1) + '" height="' + fh.toFixed(1) + '"/>');
    }

    if (vert && ocupaW > W + EPS){
      s.push('<rect x="' + (W*S).toFixed(1) + '" y="0" width="' + (w - W*S).toFixed(1) + '" height="' + h.toFixed(1) + '" fill="url(#hachura)"/>');
    }
    if (!vert && ocupaL > L + EPS){
      s.push('<rect x="0" y="' + (L*S).toFixed(1) + '" width="' + w.toFixed(1) + '" height="' + (h - L*S).toFixed(1) + '" fill="url(#hachura)"/>');
    }

    for (var j = 1; j < p.faixas; j++){
      var d = j * LARGURA_ROLO * S;
      if (vert) s.push('<line class="emenda" x1="' + d.toFixed(1) + '" y1="0" x2="' + d.toFixed(1) + '" y2="' + h.toFixed(1) + '"/>');
      else      s.push('<line class="emenda" x1="0" y1="' + d.toFixed(1) + '" x2="' + w.toFixed(1) + '" y2="' + d.toFixed(1) + '"/>');
    }

    s.push('<rect class="area" x="0" y="0" width="' + (W*S).toFixed(1) + '" height="' + (L*S).toFixed(1) + '"/>');
    s.push('<text x="' + (W*S/2).toFixed(1) + '" y="-10" text-anchor="middle">' + fmt(W) + ' m</text>');
    s.push('<text transform="translate(-10,' + (L*S/2).toFixed(1) + ') rotate(-90)" text-anchor="middle">' + fmt(L) + ' m</text>');
    s.push('</g></svg>');
    return s.join("");
  }

  /* ===== render ===== */
  var atual = null;

  function calcular(){
    if (!el("ent-largura")) return;   /* página sem calculadora */
    var W = toNum(el("ent-largura").value);
    var L = toNum(el("ent-comprimento").value);
    var erro = el("calc-erro");

    if (W <= 0 || L <= 0){
      erro.textContent = "Informe a largura e o comprimento do espaço, em metros.";
      return;
    }
    if (W > 200 || L > 200){
      erro.textContent = "Para áreas acima de 200 m de lado, fale com a equipe pelo WhatsApp.";
      return;
    }
    erro.textContent = "";

    var area = W * L;
    var plano = planejar(W, L);
    var r = plano.rec, a = plano.alt;
    /* três números distintos: área real, grama para a instalação (faixas
       inteiras) e compra recomendada (m² inteiros, arredondado para cima) */
    var instalacao = r.m2;
    var compra = Math.max(1, Math.ceil(instalacao - EPS));
    var sobra = instalacao - area;
    var pct = area > 0 ? (sobra / area) * 100 : 0;
    var rl = rolos(compra);
    var areaCola = Math.max(1, Math.ceil(area - EPS));
    var colaMax = cola(areaCola, true);
    var colaMin = cola(areaCola, false);

    el("res-area").textContent = fmt(area) + " m²";
    el("res-compra").innerHTML = fmt(compra, 0) + ' <small>m²</small>';
    el("res-eq").textContent = "Vendido em m² inteiros · rolo de " + fmt(LARGURA_ROLO, 0) + " m de largura";
    el("res-instalacao").textContent = fmt(instalacao) + " m²";
    el("res-faixas").textContent = r.faixas + (r.faixas === 1 ? " faixa" : " faixas") + " de " + fmt(r.orientacao === "vertical" ? L : W) + " m";
    el("res-emendas").textContent = r.emendas === 0 ? "Nenhuma — peça única" : r.emendas + (r.emendas === 1 ? " emenda" : " emendas");
    el("res-sobra").textContent = sobra < 0.005 ? "Sem sobra" : fmt(sobra) + " m² (" + fmt(pct, 0) + "%)";
    el("res-rolos").textContent = (rl.total === 1 ? "1 rolo ou volume: " : rl.total + " rolos ou volumes: ") + rl.partes.join(" + ") + ".";
    el("res-cola").textContent = "Para " + fmt(areaCola, 0) + " m²: " + colaMax.texto + " (rendimento máximo estimado).";
    el("res-cola-margem").textContent = colaMin.texto === colaMax.texto ?
      "Com margem de segurança (rendimento mínimo): a mesma quantidade." :
      "Com margem de segurança (rendimento mínimo): " + colaMin.texto + ".";

    el("diagrama").innerHTML = diagrama(r, W, L);

    var alt = el("res-alternativa");
    if (a.linear !== r.linear || a.emendas !== r.emendas){
      alt.textContent = "Outra orientação possível: " + a.faixas + " faixas no sentido " +
        (a.orientacao === "vertical" ? "do comprimento" : "da largura") + " — " + fmt(a.m2) +
        " m² de grama e " + a.emendas + (a.emendas === 1 ? " emenda" : " emendas") +
        ". A sugerida acima equilibra material e número de emendas.";
    } else {
      alt.textContent = "Nas duas orientações o resultado é o mesmo.";
    }

    /* explicador honesto: a conta ingênua */
    var corpo = el("porque-corpo");
    if (compra > area + 0.005){
      corpo.innerHTML = '<p>Largura × comprimento dá <span class="mono">' + fmt(area) + ' m²</span>, mas o rolo tem largura fixa de 2 m. ' +
        'Para cobrir o espaço são necessárias ' + r.faixas + ' faixas inteiras, e a última sobra para fora. ' +
        'Por isso a grama necessária é <span class="mono">' + fmt(instalacao) + ' m²</span> — ' +
        'comprar só a área real deixaria o espaço descoberto.</p>';
    } else {
      corpo.innerHTML = '<p>Neste caso a área fecha exatamente em faixas de 2 m, então a área real e a grama necessária coincidem: <span class="mono">' + fmt(compra, 0) + ' m²</span>. ' +
        'Isso é exceção — na maioria das medidas a última faixa sobra, e a conta pela área subestima o material.</p>';
    }

    atual = {W:W, L:L, area:area, r:r, sobra:sobra, instalacao:instalacao, compra:compra, rolos:rl, cola:colaMax, colaMin:colaMin, areaCola:areaCola};
  }

  /* ===== whatsapp ===== */
  var MENSAGENS = {
    topo: "Olá! Vim pelo site " + SITE + " e gostaria de um orçamento de grama sintética.",
    hero: "Olá! Vim pelo site " + SITE + ". Quero solicitar um orçamento de grama sintética.",
    transformar: "Olá! Quero transformar meu espaço com grama sintética. Pode me ajudar a escolher?",
    orientacao: "Olá! Não sei qual grama sintética escolher e gostaria de orientação para a minha aplicação.",
    projeto: "Olá! Quero consultar um projeto de grama sintética (material e instalação).",
    final: "Olá! Quero receber um orçamento de grama sintética. Vou enviar as medidas e uma foto do espaço.",
    colas: "Olá! Vi no site a linha de colas de contato Quimicolla e gostaria de consultar valores e orientações de uso.",
    rodape: "Olá! Vim pelo site " + SITE + "."
  };

  function mensagem(origem, alvo){
    if (origem === "modelo" && alvo && alvo.getAttribute("data-modelo")){
      return "Olá! Vim pelo site " + SITE + " e gostaria de um orçamento da " +
        alvo.getAttribute("data-modelo") + ". Pode me orientar?";
    }
    if (origem === "calculadora"){
      if (!atual) return "Olá! Quero ajuda para calcular a metragem de grama sintética do meu espaço.";
      var r = atual.r;
      return "Olá! Usei a calculadora do site " + SITE + ".\n\n" +
        "Espaço: " + fmt(atual.W) + " m x " + fmt(atual.L) + " m\n" +
        "Área real: " + fmt(atual.area) + " m²\n" +
        "Grama estimada para a instalação: " + fmt(atual.instalacao) + " m² (" + r.faixas + " faixas de 2 m, " + r.emendas + (r.emendas === 1 ? " emenda" : " emendas") + ")\n" +
        "Quantidade recomendada para compra: " + fmt(atual.compra, 0) + " m²\n" +
        "Rolos (estimativa): " + atual.rolos.total + " — " + atual.rolos.partes.join(" + ") + "\n" +
        "Cola Quimicolla para " + fmt(atual.areaCola, 0) + " m²: " + atual.cola.texto + " (com margem de segurança: " + atual.colaMin.texto + ")\n\n" +
        "Quero confirmar as quantidades e receber o orçamento.";
    }
    return MENSAGENS[origem] || MENSAGENS.topo;
  }

  var toastTimer = null;
  function mostrarToast(texto){
    var t = el("toast");
    el("toast-msg").textContent = texto;
    t.hidden = false;
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function(){ t.hidden = true; }, 7000);
  }

  function abrirZap(origem, alvo){
    var texto = mensagem(origem, alvo);
    if (!WHATSAPP){
      mostrarToast(texto);
      return;
    }
    window.open("https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(texto), "_blank", "noopener");
  }

  document.addEventListener("click", function(e){
    var alvo = e.target.closest ? e.target.closest("[data-zap]") : null;
    if (alvo){
      e.preventDefault();
      abrirZap(alvo.getAttribute("data-zap"), alvo);
    }
  });
  if (el("fab")) el("fab").addEventListener("click", function(){ abrirZap("rodape"); });

  /* ===== eventos ===== */
  if (el("ent-largura")){
    el("ent-largura").addEventListener("input", calcular);
    el("ent-comprimento").addEventListener("input", calcular);
    calcular();
  }

  /* nota de revisão aberta na primeira visita */
  try{
    if (el("notas-revisao") && !localStorage.getItem("mg-notas-vistas")){
      el("notas-revisao").open = true;
      localStorage.setItem("mg-notas-vistas", "1");
    }
  }catch(e){ /* storage indisponível — segue sem memória */ }
})();
