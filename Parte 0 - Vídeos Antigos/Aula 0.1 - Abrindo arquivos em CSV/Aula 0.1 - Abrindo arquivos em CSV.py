# Importando biblioteca pandas
import pandas as pd

# Abrindo arquivo em CSV
df = pd.read_csv("Dados aula 1.csv", encoding="UTF-8", sep=";", header=0)

# printando apenas as 5 primeiras linhas do df
print(df.head())

# printando o nome de todas as colunas presentes no df
print(df.columns)

# printando apenas algumas colunas e linhas do df
df_2 = pd.read_csv("Dados aula 1.csv", encoding="UTF-8", sep=";", header=0,
                   usecols=['AddressID', 'AddressLine1'], nrows=10)
print(df_2)
