import numpy as np
import pandas as pd


def lin():
    print("-=" * 100)


df1 = pd.Series(np.random.randn(5))
df2 = pd.Series(np.random.randn(5))

print(df1 * df2)
lin()
df = pd.read_excel(r"C:\Users\jorge\OneDrive\Área de Trabalho\Logimatec\lista.xlsx", header=1)

x = pd.DataFrame(df)

print(x.columns)
lin()
print(x)
lin()
print(x.head())
