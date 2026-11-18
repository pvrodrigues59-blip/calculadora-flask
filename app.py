from flask import Flask, request, jsonify, render_template
import operacoes  # importa funções do arquivo separado

# Como executar:
# 1. Certifique-se de ter o Flask instalado: pip install flask
# 2. Execute este arquivo: python app.py
# python.exe -m pip install --upgrade pip

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Página de soma
@app.route("/soma")
def soma_page():
    return render_template("soma.html")

@app.route("/api/soma", methods=["POST"])
def soma():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])
    resultado = operacoes.calcular_soma(valor1, valor2)
    return jsonify({"resultado": resultado})

# Página de subtração
@app.route("/subtracao")
def subtracao_page():
    return render_template("subtracao.html")

@app.route("/api/subtracao", methods=["POST"])
def subtracao():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])
    resultado = operacoes.calcular_subtracao(valor1, valor2)
    return jsonify({"resultado": resultado})

# Página de multiplicação
@app.route("/multiplicacao")
def multiplicacao_page():
    return render_template("multiplicacao.html")

@app.route("/api/multiplicacao", methods=["POST"])
def multiplicacao():
    try:
        dados = request.get_json(silent=True) or {}
        valor1 = float(dados["valor1"])
        valor2 = float(dados["valor2"])
        resultado = operacoes.calcular_multiplicacao(valor1, valor2)
        return jsonify({"resultado": resultado})
    except (KeyError, ValueError, TypeError):
        return jsonify({"erro": "Informe dois números válidos."}), 400

# Página de divisão
@app.route("/divisao")
def divisao_page():
    return render_template("divisao.html")

@app.route("/api/divisao", methods=["POST"])
def divisao():
    try:
        dados = request.get_json(silent=True) or {}
        valor1 = float(dados["valor1"])
        valor2 = float(dados["valor2"])
        resultado = operacoes.calcular_divisao(valor1, valor2)
        return jsonify({"resultado": resultado})
    except ZeroDivisionError:
        return jsonify({"erro": "Não é possível dividir por zero."}), 400
    except (KeyError, ValueError, TypeError):
        return jsonify({"erro": "Informe dois números válidos."}), 400

if __name__ == "__main__":
    app.run(debug=True)
