import pandas as pd


# Verficando a presença de mais de uma aba dentro do arquivo excel
abas = pd.ExcelFile("Dados Excel.xlsx")
nomesDasAbas = abas.sheet_names

# Printando nomes das abas presenes no arquivo excel
print(nomesDasAbas)

# Printando apenas uma aba específica do arquivo excel
df = pd.read_excel("Dados Excel.xlsx", sheet_name=1)
print(df)

# Separando as abas do arquivo em excel
aba1 = abas.parse("Plan1")
aba2 = abas.parse("Aba2")
print(aba2)
