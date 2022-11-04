import numpy as np
import pandas as pd


def lin():
    print("-=" * 100)


s1 = pd.Series([1, 2, 3, 4, 5], name='c1')  # criando coluna c1 com dados em lista
s2 = pd.Series([10, 20, 30, 40, 50], name='c2')  # criando coluna c2 com dados em lista

table = pd.DataFrame({s1.name: s1, s2.name: s2})    # criando um DataFrame a partir de c1 e c2

print(table)
lin()
print(table["c2"][2])   # retornando um dado específico de uma coluna
lin()
table['c3'] = "churros"
print(table)
lin()
table['c1*c2'] = table["c1"] * table["c2"]
print(table)
lin()
table.insert(1, 'Entrão', 'Isso aí')
print(table)
lin()
del table["c1*c2"]
print(table)
