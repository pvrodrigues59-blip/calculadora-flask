# Arquivo com funções matemáticas

def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b

def calcular_multiplicacao(a, b):
    return a * b

def calcular_divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
