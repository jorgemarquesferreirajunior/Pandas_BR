import pandas as pd

#pd.set_option("display.max_columns", None)

# abrindo arquivo
df = pd.read_excel("Dados.xlsx")

# ordenando dados a partir da coluna "FirstName"
ordenandos = df.sort_values("FirstName")  # Esse comando nao altera o df, apenas mostra ordenado
print(ordenandos.iloc[:10, 1:7])  # filtrando algumas linhas e colunas também

print("*%" * 50)
# ordenando a partir de duas colunas ou mais:
ordenandos_2 = df.sort_values(by=["FirstName", "LastName"])

print(ordenandos_2.iloc[:10, 4:])

print("*%" * 50)
# selecionando a ordem ascendente ou descendente:
ordenandos_3 = df.sort_values(by=["FirstName", "LastName"], ascending=[False, True])
print(ordenandos_3[["FirstName", "LastName"]].head())

