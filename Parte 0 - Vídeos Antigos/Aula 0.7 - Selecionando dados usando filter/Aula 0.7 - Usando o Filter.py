import pandas as pd

df = pd.read_csv("bank.csv", encoding="UTF-8", sep=";")

# outra forma de mostrar apenas algumas colunas, usando o filter
df_1 = df.filter(items=['job', 'marital']).head()
print(df_1)

print("*%" * 50)

print(df.head())

print("*%" * 50)
# usando o like - retorna as colunas c que apresentam a string selecionada:
df_2 = df.filter(like="day")
print(df_2.head())
















