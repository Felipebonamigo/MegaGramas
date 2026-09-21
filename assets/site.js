(function(){
  "use strict";

  /* ===== configuração ===== */
  var WHATSAPP = "";                 /* ex.: "5551999990000" — preencher para ativar os botões */
  var SITE = "megagramas.com.br";
  var LARGURA_ROLO = 2;              /* metros — largura fixa do rolo */
  var LINEAR_POR_VOLUME = 25;        /* metros lineares por volume = 50 m² */
  var PESO_EMENDA = 1.5;             /* quanto uma emenda "custa", em metros lineares equivalentes */
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
    var emendas = Math.max(0, faixas - 1);
    return {
      faixas: faixas,
      linear: linear,
      emendas: emendas,
      m2: linear * LARGURA_ROLO,
      volumes: Math.ceil(linear / LINEAR_POR_VOLUME - EPS),
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
    var sobra = r.m2 - area;
    var pct = area > 0 ? (sobra / area) * 100 : 0;

    el("res-linear").innerHTML = fmt(r.linear) + ' <small>m lineares</small>';
    el("res-eq").textContent = "Rolo de 2,00 m de largura · equivale a " + fmt(r.m2) + " m² · " +
      (r.volumes === 1 ? "1 volume" : r.volumes + " volumes");
    el("res-area").textContent = fmt(area) + " m²";
    el("res-faixas").textContent = r.faixas + (r.faixas === 1 ? " faixa" : " faixas") + " de " + fmt(r.orientacao === "vertical" ? L : W) + " m";
    el("res-emendas").textContent = r.emendas === 0 ? "Nenhuma — peça única" : r.emendas + (r.emendas === 1 ? " emenda" : " emendas");
    el("res-sobra").textContent = sobra < 0.005 ? "Sem sobra" : fmt(sobra) + " m² (" + fmt(pct, 0) + "%)";

    el("diagrama").innerHTML = diagrama(r, W, L);

    var alt = el("res-alternativa");
    if (a.linear !== r.linear || a.emendas !== r.emendas){
      alt.textContent = "Outra orientação possível: " + a.faixas + " faixas no sentido " +
        (a.orientacao === "vertical" ? "do comprimento" : "da largura") + " — " + fmt(a.linear) +
        " m lineares e " + a.emendas + (a.emendas === 1 ? " emenda" : " emendas") +
        ". A sugerida acima equilibra material e número de emendas.";
    } else {
      alt.textContent = "Nas duas orientações o resultado é o mesmo.";
    }

    /* explicador honesto: a conta ingênua */
    var ingenuo = area / LARGURA_ROLO;
    var corpo = el("porque-corpo");
    if (ingenuo < r.linear - 0.005){
      corpo.innerHTML = '<p>Dividir a área por 2 daria <span class="mono">' + fmt(ingenuo) + ' m lineares</span> — e esse material <strong style="color:#fff">não cobriria o espaço</strong>. ' +
        'Como o rolo tem largura fixa de 2 m, a área de ' + fmt(W) + ' m precisa de ' + r.faixas + ' faixas inteiras, ' +
        'e a última sobra para fora. O número certo é <span class="mono">' + fmt(r.linear) + ' m lineares</span>, ' +
        fmt(r.linear - ingenuo) + ' m a mais.</p>';
    } else {
      corpo.innerHTML = '<p>Neste caso a área fecha exatamente em faixas de 2 m, então a divisão simples coincide com o cálculo por faixas: <span class="mono">' + fmt(r.linear) + ' m lineares</span>. ' +
        'Isso é exceção — na maioria das medidas a última faixa sobra, e a conta por área subestima o material.</p>';
    }

    atual = {W:W, L:L, area:area, r:r, sobra:sobra};
  }

  /* ===== whatsapp ===== */
  var MENSAGENS = {
    topo: "Olá! Vim pelo site " + SITE + " e gostaria de um orçamento de grama sintética.",
    hero: "Olá! Vim pelo site " + SITE + ". Quero solicitar um orçamento de grama sintética.",
    transformar: "Olá! Quero transformar meu espaço com grama sintética. Pode me ajudar a escolher?",
    orientacao: "Olá! Não sei qual grama sintética escolher e gostaria de orientação para a minha aplicação.",
    projeto: "Olá! Quero consultar um projeto de grama sintética (material e instalação).",
    final: "Olá! Quero receber um orçamento de grama sintética. Vou enviar as medidas e uma foto do espaço.",
    rodape: "Olá! Vim pelo site " + SITE + "."
  };

  function mensagem(origem){
    if (origem === "calculadora"){
      if (!atual) return "Olá! Quero ajuda para calcular a metragem de grama sintética do meu espaço.";
      var r = atual.r;
      return "Olá! Usei a calculadora do site " + SITE + ".\n\n" +
        "Espaço: " + fmt(atual.W) + " m x " + fmt(atual.L) + " m (" + fmt(atual.area) + " m²)\n" +
        "Sugestão da calculadora: " + fmt(r.linear) + " m lineares = " + fmt(r.m2) + " m²\n" +
        "Faixas: " + r.faixas + " · Emendas: " + r.emendas + " · Sobra: " + fmt(atual.sobra) + " m²\n\n" +
        "Quero confirmar a quantidade e receber o orçamento.";
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

  function abrirZap(origem){
    var texto = mensagem(origem);
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
      abrirZap(alvo.getAttribute("data-zap"));
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
