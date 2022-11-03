import pandas as pd
import numpy as np


lista1 = [1, 4, 3, 6, 8, 9]

lista = [1, 4, "tesla", 3, 6.3, 8, 9]

exemplo = pd.Series(lista)

# print(exemplo)

print(pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"]))   # Utilizando/Configurando Índices

