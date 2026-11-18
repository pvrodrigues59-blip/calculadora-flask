function calcularSoma() {
    const v1 = document.getElementById("valor1").value;
    const v2 = document.getElementById("valor2").value;

    fetch("/api/soma", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ valor1: v1, valor2: v2 })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("resultado").innerText = "Resultado: " + data.resultado;
    });
}

function calcularSubtracao() {
    const v1 = document.getElementById("valor1").value;
    const v2 = document.getElementById("valor2").value;

    fetch("/api/subtracao", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ valor1: v1, valor2: v2 })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("resultado").innerText = "Resultado: " + data.resultado;
    });
}

function calcularMultiplicacao() {
    calcularOperacao("multiplicacao");
}

async function calcularOperacao(operacao) {
    const valor1 = document.getElementById("valor1").value;
    const valor2 = document.getElementById("valor2").value;
    const saida = document.getElementById("resultado");

    if (valor1.trim() === "" || valor2.trim() === "") {
        saida.textContent = "Informe os dois valores.";
        return;
    }

    try {
        const resposta = await fetch("/api/" + operacao, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ valor1, valor2 })
        });
        const dados = await resposta.json();
        saida.textContent = resposta.ok
            ? "Resultado: " + dados.resultado
            : "Erro: " + (dados.erro || "Não foi possível calcular.");
    } catch (erro) {
        saida.textContent = "Erro de comunicação com o servidor.";
    }
}

function calcularDivisao() {
    calcularOperacao("divisao");
}
