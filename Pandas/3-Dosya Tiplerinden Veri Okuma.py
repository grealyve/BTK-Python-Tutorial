import pandas as pd
import sqlite3

#df = pd.read_csv("USvideos.csv")
# df = pd.read_json("US_category_id.json", encoding="UTF-8")
# df = pd.read_excel("sample.xlsx")

connection = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM students", connection)

print(df)