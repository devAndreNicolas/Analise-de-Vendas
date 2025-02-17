import pandas as pd
import calendar
import matplotlib.pyplot as plt
import seaborn as sns

class AnalisadorDeVendas:
    def __init__(self, caminho_arquivo):
        # Carregar os dados limpos
        self.df = pd.read_csv(caminho_arquivo, sep=";")
        self.df["Data da Venda"] = pd.to_datetime(self.df["Data da Venda"])
        self.df["Mês"] = self.df["Data da Venda"].dt.month
        self.df["Ano"] = self.df["Data da Venda"].dt.year

    def produtos_mais_vendidos(self):
        # Produtos mais vendidos
        produtos_mais_vendidos = (
            self.df.groupby("Produto")["Quantidade Vendida"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        return produtos_mais_vendidos

    def mes_com_maior_volume_de_vendas(self):
        # Mês com maior volume de vendas
        vendas_por_mes = (
            self.df.groupby(["Ano", "Mês"])["Quantidade Vendida"]
            .sum()
            .reset_index()
            .sort_values(by=["Ano", "Mês"])
        )
        mes_maior_vendas = vendas_por_mes.loc[vendas_por_mes["Quantidade Vendida"].idxmax()]
        return mes_maior_vendas

    def receita_por_regiao(self):
        # Receita por região
        receita_por_regiao = (
            self.df.groupby("Região de Venda")["Receita"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        return receita_por_regiao

    def sazonalidade_nas_vendas(self):
        # Sazonalidade nas vendas (total por mês)
        vendas_sazonalidade = (
            self.df.groupby("Mês")["Quantidade Vendida"].sum().sort_index().reset_index()
        )
        vendas_sazonalidade["Mês"] = vendas_sazonalidade["Mês"].apply(
            lambda x: calendar.month_abbr[x]
        )
        return vendas_sazonalidade

    def total_de_vendas_por_mes(self):
        # Total de vendas por mês
        total_vendas_mes = (
            self.df.groupby(["Ano", "Mês"])["Receita"]
            .sum()
            .reset_index()
            .sort_values(by=["Ano", "Mês"])
        )
        total_vendas_mes.rename(columns={"Receita": "Total de Vendas"}, inplace=True)
        total_vendas_mes["Mês"] = total_vendas_mes["Mês"].apply(lambda x: calendar.month_abbr[x])
        total_vendas_mes["Período"] = total_vendas_mes["Mês"] + " " + total_vendas_mes["Ano"].astype(str)
        total_vendas_mes = total_vendas_mes[["Período", "Total de Vendas"]]
        return total_vendas_mes

    def lucro_por_categoria(self):
        # Categorias mais lucrativas
        lucro_por_categoria = (
            self.df.groupby("Categoria")["Receita"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        return lucro_por_categoria

    def crescimento_mensal(self):
        # Crescimento mensal
        total_vendas_mes = self.total_de_vendas_por_mes()
        total_vendas_mes["Crescimento Mensal (%)"] = (
            total_vendas_mes["Total de Vendas"].pct_change().fillna(0) * 100
        )
        total_vendas_mes["Crescimento Mensal (%)"] = total_vendas_mes["Crescimento Mensal (%)"].round(2)
        return total_vendas_mes

    def gerar_graficos(self):
        # Gráficos de EDA
        total_vendas_mes = self.total_de_vendas_por_mes()
        produtos_mais_vendidos = self.produtos_mais_vendidos()

        # 1. Gráfico de linha para evolução de vendas ao longo do tempo
        plt.figure(figsize=(10, 6))
        sns.lineplot(x="Período", y="Total de Vendas", data=total_vendas_mes, marker="o", color="b")
        plt.title("Evolução de Vendas ao Longo do Tempo")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # 2. Gráfico de barras para mostrar os produtos mais vendidos
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Quantidade Vendida", y="Produto", data=produtos_mais_vendidos, palette="viridis")
        plt.title("Produtos Mais Vendidos")
        plt.tight_layout()
        plt.show()

        # 3. Mapa de calor para vendas por categoria e região
        vendas_categoria_regiao = self.df.groupby(["Categoria", "Região de Venda"])["Receita"].sum().unstack()
        plt.figure(figsize=(12, 7))
        sns.heatmap(vendas_categoria_regiao, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=0.5)
        plt.title("Vendas por Categoria e Região")
        plt.tight_layout()
        plt.show()

        # 4. Tabela dinâmica para análise detalhada por mês e produto
        tabela_dinamica = self.df.pivot_table(values="Receita", index="Produto", columns="Mês", aggfunc="sum", fill_value=0)
        plt.figure(figsize=(12, 7))
        sns.heatmap(tabela_dinamica, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=0.5)
        plt.title("Vendas por Produto e Mês")
        plt.tight_layout()
        plt.show()

        # 5. Gráfico de linha para crescimento mensal
        crescimento_mensal_df = self.crescimento_mensal()

        plt.figure(figsize=(10, 6))
        sns.lineplot(x="Período", y="Crescimento Mensal (%)", data=crescimento_mensal_df, marker="o", color="r")
        plt.title("Crescimento Mensal de Vendas")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def resumo_eda(self):
        # Exibe o resumo da EDA
        print("Produtos mais vendidos:")
        print(self.produtos_mais_vendidos())
        print("\nMês com maior volume de vendas:")
        print(self.mes_com_maior_volume_de_vendas())
        print("\nReceita por região:")
        print(self.receita_por_regiao())
        print("\nSazonalidade nas vendas (total por mês):")
        print(self.sazonalidade_nas_vendas())
        print("\nTotal de vendas por mês:")
        print(self.total_de_vendas_por_mes())
        print("\nCategorias mais lucrativas:")
        print(self.lucro_por_categoria())
        print("\nCrescimento mensal de vendas (em ordem cronológica):")
        print(self.crescimento_mensal())

        print("\nResumo da EDA concluído!")


# Usando a classe para realizar a análise
analise = AnalisadorDeVendas("csv/dados_vendas_ficticias_limpos.csv")

# Mostrar resumo EDA
analise.resumo_eda()

# Gerar gráficos
analise.gerar_graficos()