import pandas as pd

# mostrando todas as colunas e linhas no terminal
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# abrindo o arquivo
dados = pd.read_excel("Dados.xlsx")

# selecionando uma coluna
nomes = dados["FirstName"].head()
sobrenomes = dados.MiddleName
print(sobrenomes.head())    # atributo .head() serve para mostrar apenas as 5 primeiras linhas do dataframe


# selecionando um range de colunas
nomes_sobrenomes = dados[["FirstName", "MiddleName"]]
n2 = dados[["FirstName", "MiddleName"]].head()
print(nomes_sobrenomes.head())
print(type(nomes_sobrenomes.head()))

# Adicionando uma coluna
dados["NomeCompleto"] = dados["FirstName"] + " " + dados["MiddleName"] + " " + dados["LastName"]

print(dados["NomeCompleto"].head())

