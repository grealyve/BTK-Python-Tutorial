import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns= ["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns         # kolon isimlerini çeker
result = df.head(10)        # baştaki 10 satırı çevirir default değeri 5
result = df.tail()
result = df.Column1.head()      # df["Column1"].head()
result = df[["Column1","Column2"]].head()
result = df[["Column1","Column2"]].tail()
result = df[5:15][["Column1","Column2"]].head()     # 5'den 15'e kadar 5 tane değerleri çekersin

result = df > 50
result = df[df > 50]
result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column1"]> 50) & (df["Column1"]<= 70)] # and
result = df[(df["Column1"]> 50) | (df["Column2"]<= 70)] # or
result = df[(df["Column1"]> 50) | (df["Column2"]<= 70)][["Column1","Column2"]]
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]

print(result)