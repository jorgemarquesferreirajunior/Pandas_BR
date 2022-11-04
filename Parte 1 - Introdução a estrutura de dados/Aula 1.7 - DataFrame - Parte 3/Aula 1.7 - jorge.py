def lin():
    print("-" * 100)


# importando bibliotecas
import pandas as pd
import numpy as np

# abrindo arquivo da base aluguel
file = pd.read_csv(r"C:\Users\jorge\OneDrive\Documentos\GitHub\Pandas_BR\bases\alugueis\houses_to_rent.csv", header=0,
                   encoding="UTF-8", sep=",")

print(file)
lin()
print(file["hoa"])
lin()
print(file['hoa'].apply(lambda x: x.replace("R$", "")))  # substituindo "R$" por "" - nao altera a base de dados!!
lin()
file['hoa_tratado'] = file['hoa'].apply(lambda x: x.replace("R$", ""))
print(file)
lin()
file2 = file[["hoa_tratado", "rent amount", "property tax"]].applymap(lambda x: x.replace("R$", ""))
file2['hoa'] = file["hoa"]
print(file2.head())
lin()
del file2["hoa"]
print(file2)
