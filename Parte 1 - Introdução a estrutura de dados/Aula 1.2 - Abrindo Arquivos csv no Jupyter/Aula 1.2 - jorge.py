import pandas as pd
from pathlib import Path
import os

path = Path(os.getcwd())
path = str(path.parent.parent) + '\\bases\\alugueis\\houses_to_rent.csv'
print(path)

df = pd.read_csv(path)

print(df)
