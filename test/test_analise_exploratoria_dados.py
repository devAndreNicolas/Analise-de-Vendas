#Validar se as funções de agregação (ex: produtos mais vendidos, receita por região) retornam dados corretamente.
#Confirmar se os gráficos são gerados sem erros.
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from analise_exploratoria_dados import AnalisadorDeVendas

class TestAnalisadorDeVendas(unittest.TestCase):
    def setUp(self):
        # Setup inicial com o arquivo de dados limpos
        self.analise = AnalisadorDeVendas("csv/dados_vendas_ficticias_limpos.csv")

    def test_produtos_mais_vendidos(self):
        # Verifica se a lista de produtos mais vendidos é gerada corretamente
        produtos = self.analise.produtos_mais_vendidos()
        self.assertTrue(isinstance(produtos, pd.DataFrame))
        self.assertGreater(len(produtos), 0)

    def test_mes_com_maior_volume_de_vendas(self):
        # Verifica se o mês com maior volume de vendas é retornado corretamente
        mes_maior_vendas = self.analise.mes_com_maior_volume_de_vendas()
        self.assertTrue("Ano" in mes_maior_vendas)
        self.assertTrue("Mês" in mes_maior_vendas)
        self.assertTrue("Quantidade Vendida" in mes_maior_vendas)

    def test_receita_por_regiao(self):
        # Verifica se a receita por região é calculada corretamente
        receita_regiao = self.analise.receita_por_regiao()
        self.assertTrue(isinstance(receita_regiao, pd.DataFrame))
        self.assertGreater(len(receita_regiao), 0)

    def test_sazonalidade_nas_vendas(self):
        # Verifica se a sazonalidade das vendas é calculada corretamente
        sazonalidade = self.analise.sazonalidade_nas_vendas()
        self.assertTrue(isinstance(sazonalidade, pd.DataFrame))
        self.assertGreater(len(sazonalidade), 0)

    def test_total_de_vendas_por_mes(self):
        # Verifica se o total de vendas por mês é calculado corretamente
        vendas_mes = self.analise.total_de_vendas_por_mes()
        self.assertTrue(isinstance(vendas_mes, pd.DataFrame))
        self.assertGreater(len(vendas_mes), 0)

    def test_lucro_por_categoria(self):
        # Verifica se o lucro por categoria é calculado corretamente
        lucro_categoria = self.analise.lucro_por_categoria()
        self.assertTrue(isinstance(lucro_categoria, pd.DataFrame))
        self.assertGreater(len(lucro_categoria), 0)

    def test_crescimento_mensal(self):
        # Verifica se o crescimento mensal é calculado corretamente
        crescimento = self.analise.crescimento_mensal()
        self.assertTrue(isinstance(crescimento, pd.DataFrame))
        self.assertGreater(len(crescimento), 0)

if __name__ == "__main__":
    unittest.main()