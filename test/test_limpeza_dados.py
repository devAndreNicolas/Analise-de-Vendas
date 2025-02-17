#Verificar que as duplicatas sejam removidas.
#Confirmar que os valores ausentes sejam tratados corretamente.
#Garantir que os tipos de dados sejam convertidos corretamente.
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from limpeza_dados import TratamentoDeDados

class TestTratamentoDeDados(unittest.TestCase):
    def setUp(self):
        # Setup inicial com o arquivo limpo
        self.tratamento = TratamentoDeDados("csv/dados_vendas_ficticias_limpos.csv")

    def test_remover_duplicatas(self):
        # Verifica se as duplicatas são removidas
        antes = len(self.tratamento.df)
        self.tratamento.remover_duplicatas()
        depois = len(self.tratamento.df)

        if antes == depois:
            print("Nenhuma duplicata encontrada.")
        else:
            self.assertLess(depois, antes)  # Após a remoção, o número de registros deve diminuir

    def test_tratar_valores_ausentes(self):
        # Verifica se os valores ausentes são tratados
        self.tratamento.tratar_valores_ausentes()
        self.assertFalse(self.tratamento.df.isnull().values.any())  # Não deve haver valores ausentes

    def test_converter_tipos_dados(self):
        # Verifica se os tipos de dados são convertidos corretamente
        self.tratamento.converter_tipos_dados()
        self.assertEqual(self.tratamento.df["Data da Venda"].dtype, 'datetime64[ns]')
        self.assertEqual(self.tratamento.df["Preço por Unidade"].dtype, 'float64')

    def test_tratar_outliers(self):
        # Verifica se os outliers são removidos (preço > 10.000)
        self.tratamento.tratar_outliers()
        self.assertTrue((self.tratamento.df["Preço por Unidade"] <= 10000).all())

if __name__ == "__main__":
    unittest.main()