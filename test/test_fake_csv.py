#Garantir que o número de registros gerados seja o esperado.
#Confirmar se os dados são gerados de forma consistente (produtos, categorias, regiões, etc.).
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from fake_csv import GeradorVendas, Produto, Venda  # Importar as classes relevantes

class TestGeradorVendas(unittest.TestCase):
    def setUp(self):
        # Setup para cada teste, pode ser reutilizado para todos
        self.gerador = GeradorVendas()

    def test_gerar_vendas_numero_correto(self):
        # Verifica se o número de vendas geradas é o correto
        vendas = self.gerador.gerar_vendas(500)
        self.assertEqual(len(vendas), 500)
    
    def test_vendas_categoria_valida(self):
        # Verifica se as vendas estão sendo geradas com categorias válidas
        vendas = self.gerador.gerar_vendas(100)
        categorias_validas = ["Eletrônicos", "Roupas", "Alimentos"]
        for venda in vendas:
            self.assertIn(venda.produto.categoria, categorias_validas)

    def test_gerar_vendas_estrutura(self):
        # Verifica a estrutura do dicionário de dados
        vendas = self.gerador.gerar_vendas(1)
        venda = vendas[0]
        self.assertTrue(hasattr(venda, 'data_venda'))
        self.assertTrue(hasattr(venda, 'produto'))
        self.assertTrue(hasattr(venda, 'quantidade_vendida'))
        self.assertTrue(hasattr(venda, 'regiao_venda'))
        self.assertTrue(hasattr(venda, 'receita'))

if __name__ == "__main__":
    unittest.main()