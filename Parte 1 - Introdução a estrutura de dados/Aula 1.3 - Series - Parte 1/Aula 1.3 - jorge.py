def lin():
    print("-=" * 100)

import pandas as pd
import numpy as np


lista1 = [1, 4, 3, 6, 8, 9]

lista = [1, 4, "tesla", 3, 6.3, 8, 9]

ex01 = pd.Series(lista)

print(ex01)

lin()

print(pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"]))   # Utilizando/Configurando Índices
# através de listas

lin()

s = pd.Series({"a": 20, "b": 34, "c": 45})
print(s)# Utilizando/Configurando Índices através de dicionários
print(s[0:1])

lin()

jorge = pd.Series(np.random.randn(5), name='jorge')
print(jorge)

lin()


