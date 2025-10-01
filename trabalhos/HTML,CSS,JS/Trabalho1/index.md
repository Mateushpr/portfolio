<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Caça-Palavras com Destaque</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
    }

    table {
      margin: 20px auto;
      border-collapse: collapse;
    }

    td {
      border: 1px solid #000;
      width: 30px;
      height: 30px;
      text-align: center;
      font-size: 18px;
      font-weight: bold;
      user-select: none;
      cursor: pointer;
      transition: background-color 0.2s;
    }

    td:hover:not(.found) {
      background-color: #d0eaff;
    }

    td.selected {
      background-color: #87ceeb;
    }

    td.found {
      background-color: #90ee90;
    }

    .word-list {
      margin-top: 20px;
    }

    .found-word {
      text-decoration: line-through;
      color: green;
    }

    button {
      margin-top: 20px;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Caça-Palavras</h1>
  <div id="word-search"></div>
  <div class="word-list" id="word-list"></div>
  <button onclick="reiniciarJogo()">Novo Jogo</button>
  <p><strong>Arraste ou toque nas letras para formar uma palavra.</strong></p>

  <script>
    const palavrasBase = ["javascript", "codigo", "logica", "função", "variavel", "objeto", "array"];
    const tamanho = 15;
    let palavras = [...palavrasBase];
    let grade = [];
    let selecionadas = [];
    let mousePressionado = false;

    function criarGrade() {
      grade = Array.from({ length: tamanho }, () => Array(tamanho).fill(''));
    }

    function colocarPalavra(palavra) {
      const direcoes = [
        { dx: 0, dy: 1 },
        { dx: 1, dy: 0 },
        { dx: 1, dy: 1 },
        { dx: -1, dy: 1 }
      ];

      palavra = palavra.toUpperCase();
      for (let tentativa = 0; tentativa < 100; tentativa++) {
        const dir = direcoes[Math.floor(Math.random() * direcoes.length)];
        const x = Math.floor(Math.random() * tamanho);
        const y = Math.floor(Math.random() * tamanho);
        const fimX = x + dir.dx * (palavra.length - 1);
        const fimY = y + dir.dy * (palavra.length - 1);

        if (fimX < 0 || fimX >= tamanho || fimY < 0 || fimY >= tamanho) continue;

        let podeColocar = true;
        for (let i = 0; i < palavra.length; i++) {
          const nx = x + dir.dx * i;
          const ny = y + dir.dy * i;
          const letraAtual = grade[nx][ny];
          if (letraAtual !== '' && letraAtual !== palavra[i]) {
            podeColocar = false;
            break;
          }
        }

        if (podeColocar) {
          for (let i = 0; i < palavra.length; i++) {
            const nx = x + dir.dx * i;
            const ny = y + dir.dy * i;
            grade[nx][ny] = palavra[i];
          }
          return true;
        }
      }

      console.warn("Não foi possível colocar:", palavra);
      return false;
    }

    function preencherGrade() {
      for (let i = 0; i < tamanho; i++) {
        for (let j = 0; j < tamanho; j++) {
          if (grade[i][j] === '') {
            grade[i][j] = String.fromCharCode(65 + Math.floor(Math.random() * 26));
          }
        }
      }
    }

    function exibirGrade() {
      const container = document.getElementById("word-search");
      const tabela = document.createElement("table");

      for (let i = 0; i < tamanho; i++) {
        const linha = document.createElement("tr");
        for (let j = 0; j < tamanho; j++) {
          const celula = document.createElement("td");
          celula.textContent = grade[i][j];
          celula.dataset.row = i;
          celula.dataset.col = j;

          // Eventos para mouse
          celula.addEventListener("mousedown", () => {
            mousePressionado = true;
            limparSelecao();
            adicionarSelecao(celula);
          });

          celula.addEventListener("mouseover", () => {
            if (mousePressionado && !celula.classList.contains("found")) {
              adicionarSelecao(celula);
            }
          });

          // Eventos para toque (mobile)
          celula.addEventListener("touchstart", (e) => {
            e.preventDefault();
            mousePressionado = true;
            limparSelecao();
            adicionarSelecao(celula);
          });

          celula.addEventListener("touchmove", (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            const elem = document.elementFromPoint(touch.clientX, touch.clientY);
            if (elem && elem.tagName === "TD" && !elem.classList.contains("found")) {
              adicionarSelecao(elem);
            }
          });

          linha.appendChild(celula);
        }
        tabela.appendChild(linha);
      }

      container.innerHTML = '';
      container.appendChild(tabela);

      // Finalizar seleção
      document.addEventListener("mouseup", () => {
        if (mousePressionado) {
          verificarSelecao();
          mousePressionado = false;
        }
      });

      document.addEventListener("touchend", () => {
        if (mousePressionado) {
          verificarSelecao();
          mousePressionado = false;
        }
      });
    }

    function adicionarSelecao(celula) {
      if (!selecionadas.includes(celula) && !celula.classList.contains("found")) {
        celula.classList.add("selected");
        selecionadas.push(celula);
      }
    }

    function limparSelecao() {
      selecionadas.forEach(c => c.classList.remove("selected"));
      selecionadas.length = 0;
    }

    function exibirPalavras() {
      const lista = document.getElementById("word-list");
      lista.innerHTML = "<h3>Palavras para encontrar:</h3><ul id='palavras-ul'>" +
        palavras.map(p => `<li data-word="${p.toUpperCase()}">${p.toUpperCase()}</li>`).join('') +
        "</ul>";
    }

    function verificarSelecao() {
      const palavraSelecionada = selecionadas.map(c => c.textContent).join('');
      const palavraReversa = selecionadas.map(c => c.textContent).reverse().join('');

      const encontrada = palavras.find(p => p.toUpperCase() === palavraSelecionada || p.toUpperCase() === palavraReversa);

      if (encontrada) {
        // Marcar como encontrada
        selecionadas.forEach(c => {
          c.classList.remove("selected");
          c.classList.add("found");
        });
        const li = document.querySelector(`[data-word="${encontrada.toUpperCase()}"]`);
        if (li) li.classList.add("found-word");
      } else {
        limparSelecao();
      }
    }

    function iniciarJogo() {
      palavras = [...palavrasBase];
      criarGrade();
      palavras.forEach(colocarPalavra);
      preencherGrade();
      exibirGrade();
      exibirPalavras();
    }

    function reiniciarJogo() {
      iniciarJogo();
    }

    // Iniciar na primeira vez
    iniciarJogo();
  </script>
</body>
</html>

