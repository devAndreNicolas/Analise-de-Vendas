import pandas as pd  # Importa a biblioteca pandas para manipulação de dados em DataFrame
from faker import Faker  # Importa a biblioteca Faker para gerar dados fictícios, como datas
import random  # Importa a biblioteca random para gerar números aleatórios

fake = Faker()  # Cria uma instância da classe Faker para gerar dados fictícios

# Classe Produto: Representa um produto com suas características (nome, categoria e preço)
class Produto:
    def __init__(self, nome, categoria, preco):
        self.nome = nome  # Nome do produto
        self.categoria = categoria  # Categoria do produto (Eletrônicos, Roupas, Alimentos)
        self.preco = preco  # Preço do produto

# Classe Venda: Representa uma venda de um produto, contendo informações como data da venda, produto vendido, quantidade e região
class Venda:
    def __init__(self, produto, quantidade_vendida, regiao_venda):
        # A data da venda é gerada aleatoriamente entre um ano atrás e a data atual
        self.data_venda = fake.date_between(start_date='-1y', end_date='today')
        
        self.produto = produto  # O produto que foi vendido (instância da classe Produto)
        self.quantidade_vendida = quantidade_vendida  # Quantidade de unidades do produto vendido
        self.regiao_venda = regiao_venda  # Região onde a venda ocorreu
        
        # Calcula a receita da venda multiplicando a quantidade vendida pelo preço do produto
        self.receita = self.quantidade_vendida * self.produto.preco

    def __str__(self):
        # Retorna uma string formatada com as informações da venda
        return f"{self.data_venda} - {self.produto.nome} ({self.produto.categoria}) - Quantidade: {self.quantidade_vendida} - Receita: {self.receita}"

# Classe GeradorVendas: Responsável por gerar as vendas fictícias e armazenar os dados em um DataFrame
class GeradorVendas:
    def __init__(self):
        # Definindo os produtos em listas, organizados por categoria
        self.produtos = {
            "Eletrônicos": [
                Produto("Smartphone X200", "Eletrônicos", 199.99),
                Produto("Laptop Pro 15", "Eletrônicos", 1200.50),
                Produto("Tablet S10", "Eletrônicos", 799.99),
                Produto("Smartwatch Z5", "Eletrônicos", 249.99),
                Produto("Headphones Pro", "Eletrônicos", 99.99)
            ],
            "Roupas": [
                Produto("Camiseta Polo", "Roupas", 49.99),
                Produto("Jaqueta de Couro", "Roupas", 250.00),
                Produto("Calça Jeans", "Roupas", 120.00),
                Produto("Tênis Esportivo", "Roupas", 150.00),
                Produto("Chapéu Fedora", "Roupas", 80.00)
            ],
            "Alimentos": [
                Produto("Biscoito de Chocolate", "Alimentos", 5.99),
                Produto("Suco Natural", "Alimentos", 8.99),
                Produto("Cereal Matinal", "Alimentos", 15.50),
                Produto("Pão Integral", "Alimentos", 4.50),
                Produto("Café Premium", "Alimentos", 22.99)
            ]
        }

    def gerar_vendas(self, num_vendas=500):
        # Lista para armazenar as vendas geradas
        vendas = []
        
        for _ in range(num_vendas):
            # Escolhe uma categoria aleatória
            categoria = random.choice(["Eletrônicos", "Roupas", "Alimentos"])
            
            # Escolhe um produto aleatório dentro da categoria escolhida
            produto = random.choice(self.produtos[categoria])
            
            # Gera uma quantidade aleatória de unidades vendidas (entre 1 e 20)
            quantidade_vendida = random.randint(1, 20)
            
            # Escolhe uma região de venda aleatória
            regiao_venda = random.choice(["Norte", "Sul", "Leste", "Oeste"])
            
            # Cria uma nova venda e a adiciona à lista de vendas
            venda = Venda(produto, quantidade_vendida, regiao_venda)
            vendas.append(venda)
        
        return vendas

# Instancia a classe GeradorVendas e gera as vendas
gerador = GeradorVendas()
vendas = gerador.gerar_vendas(500)

# Cria uma lista de dicionários com os dados das vendas, para ser convertida em DataFrame
dados_vendas = [{
    "Data da Venda": venda.data_venda,
    "Produto": venda.produto.nome,
    "Categoria": venda.produto.categoria,
    "Quantidade Vendida": venda.quantidade_vendida,
    "Preço por Unidade": venda.produto.preco,
    "Região de Venda": venda.regiao_venda,
    "Receita": venda.receita
} for venda in vendas]

# Cria um DataFrame com os dados das vendas
df = pd.DataFrame(dados_vendas)

# Salva o DataFrame como um arquivo CSV
df.to_csv("dados_vendas_ficticias.csv", sep=";", index=False)

# Exibe uma mensagem indicando que os dados foram gerados com sucesso
print("Dados de vendas fictícias gerados com sucesso!")