import numpy as np
import pandas as pd


def lin():
    print("-=" * 100)


s1 = pd.Series([1, 2, 3, 4, 5], name='c1')
s2 = pd.Series([10, 20, 30, 40, 50], name='c2')

table = pd.DataFrame({s1.name: s1, s2.name: s2})

print(table)
lin()
print(table["c2"][2])
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
