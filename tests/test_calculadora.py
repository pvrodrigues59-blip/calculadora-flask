import unittest
from app import app
from operacoes import calcular_multiplicacao, calcular_divisao


class CalculadoraTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_paginas(self):
        for rota in ("/", "/soma", "/subtracao", "/multiplicacao", "/divisao"):
            self.assertEqual(self.client.get(rota).status_code, 200)

    def test_operacoes(self):
        self.assertEqual(calcular_multiplicacao(3, 4), 12)
        self.assertEqual(calcular_divisao(9, 3), 3)

    def test_apis(self):
        for rota, esperado in (("/api/soma", 11), ("/api/subtracao", 5),
                                ("/api/multiplicacao", 24), ("/api/divisao", 2.6666666666666665)):
            resposta = self.client.post(rota, json={"valor1": 8, "valor2": 3})
            self.assertEqual(resposta.status_code, 200)
            self.assertAlmostEqual(resposta.json["resultado"], esperado)

    def test_divisao_zero(self):
        resposta = self.client.post("/api/divisao", json={"valor1": 8, "valor2": 0})
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("zero", resposta.json["erro"])

    def test_valores_invalidos(self):
        resposta = self.client.post("/api/multiplicacao", json={"valor1": "", "valor2": 2})
        self.assertEqual(resposta.status_code, 400)


if __name__ == "__main__":
    unittest.main()
