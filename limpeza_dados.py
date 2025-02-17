import pandas as pd  # Importa a biblioteca pandas para manipulação de dados em DataFrame

# Classe de tratamento de dados: Responsável por limpar e transformar os dados
class TratamentoDeDados:
    def __init__(self, caminho_arquivo):
        # Carrega o arquivo CSV com os dados de vendas
        self.df = pd.read_csv(caminho_arquivo, sep=";")
    
    def remover_duplicatas(self):
        # Remove as duplicatas do DataFrame
        self.df.drop_duplicates(inplace=True)
    
    def tratar_valores_ausentes(self):
        # Verifica se há valores ausentes e imprime a contagem por coluna
        print("Valores ausentes por coluna:\n", self.df.isnull().sum())
        
        # Preenche os valores ausentes com valores padrão
        self.df.fillna({
            "Produto": "Desconhecido",
            "Quantidade Vendida": 0,
            "Preço por Unidade": 0.0,
        }, inplace=True)
    
    def converter_tipos_dados(self):
        # Converte a coluna "Data da Venda" para o formato datetime
        self.df["Data da Venda"] = pd.to_datetime(self.df["Data da Venda"], errors='coerce')
        
        # Converte a coluna "Preço por Unidade" para o tipo float
        self.df["Preço por Unidade"] = pd.to_numeric(self.df["Preço por Unidade"], errors='coerce')
    
    def tratar_outliers(self):
        # Remove registros com valores absurdos de "Preço por Unidade" (acima de 10.000)
        self.df = self.df[self.df["Preço por Unidade"] <= 10000]
    
    def limpar_colunas(self):
        # Remove espaços dos nomes das colunas
        self.df.columns = self.df.columns.str.strip()
    
    def exibir_dados(self):
        # Exibe as primeiras linhas do DataFrame após o tratamento
        print("Dados após limpeza:\n", self.df.head())
    
    def salvar_dados(self, caminho_saida):
        # Salva os dados tratados em um novo arquivo CSV
        self.df.to_csv(caminho_saida, index=False, sep=";")
        print(f"Dados limpos salvos em: {caminho_saida}")

# Usando a classe TratamentoDeDados para tratar o arquivo de vendas
tratamento = TratamentoDeDados("csv\\dados_vendas_ficticias.csv")

# Executando o fluxo de tratamento de dados
tratamento.remover_duplicatas()  # Remove duplicatas
tratamento.tratar_valores_ausentes()  # Trata valores ausentes
tratamento.converter_tipos_dados()  # Converte tipos de dados
tratamento.tratar_outliers()  # Trata outliers
tratamento.limpar_colunas()  # Limpa espaços das colunas
tratamento.exibir_dados()  # Exibe os dados tratados
tratamento.salvar_dados("dados_vendas_ficticias_limpos.csv")  # Salva os dados tratados