import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index= ["A","B","C"], columns= ["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = df[["Column1","Column2"]]      # kolona göre seçme

# loc["row","column"] => loc["row"] => loc[":","column"]
result = df.loc["A"]                        # satıra göre seçme
result = df.iloc[2]                         # satırınn indexine göre seçme
# result = df.loc[:,"Column2"]
# result = df.loc[:,"Column1":"Column2"]      # aralık almak istersen
# result = df.loc[:,:"Column2"]
# result = df.loc["A":"B",:"Column2"]
result = df.loc["C","Column2"]
result = df.loc[["A","C"],["Column1","Column2"]]

df["Column4"] = pd.Series(randn(3), ["A","B","C"])
df["Column5"] = df["Column1"] + df["Column3"]       # 2 seriyi toplayıp aynı seriye ekleyebilirsin

print(df.drop("Column5", axis=1, inplace= True))       # inplace yazmazsan güncellenmez

print(df)
