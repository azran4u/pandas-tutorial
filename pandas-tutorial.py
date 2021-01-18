import os
import pandas as pd

path = os.getcwd() + '\\1.csv'
print(path)

df = pd.read_csv(path)

print(df.head(5))
