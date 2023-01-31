import pandas as pd

pd.set_option("display.max_columns", None)
df = pd.read_excel("Dados.xlsx")

# Usando Loc - selecionando um range de linhas
#print(df.loc[:6])

# Também da para usar loc em um range de colunas
print(df[["FirstName", "MiddleName"]].loc[:9])

# A linha 13 é apenas para nao mostrar todas as colunas, aparecendo as 3 primeiras e as 3 ultimas
pd.reset_option('^display.', silent=True)
print(df.loc[[1, 3, 5]])

print("---------------------")

# Selecionando linhas e colunas específicas
print(df.loc[4:6, ["FirstName", "LastName"]])

print("---------------------")

# selecionado determinadas linhas e um range de colunas
print(df.loc[4:8, "FirstName" : "LastName"])

print("---------------------")

# Usando o iloc - parecido ao loc, o iloc aceita apenas numeros para configurar o range:
print(df.iloc[1:4, 2:6])
