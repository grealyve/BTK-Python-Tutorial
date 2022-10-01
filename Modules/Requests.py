import requests
import json

# Http requesti yapabiliyorsun. Kaynak kodlarını çekiyor.

# result = requests.get("http://jsonplaceholder.typicode.com/todos")
# result = json.loads(result.text)
#
# for i in result:
#     if i["userId"] == 1:
#         print(i["title"])

# print(result)

############ EXCHANGE API ###############
# f6e16450db5ca41e4d9ce64b382fc8d9
# base EUR = 1 olarak alındı. Bu yüzden sadece eur' dan dönüşüm yapabilirsin.

result = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=f6e16450db5ca41e4d9ce64b382fc8d9")
result = json.loads(result.text)

boz = input("Bozulan döviz türü: ").upper()
al = input("Alınan döviz türü: ").upper()
miktar = int(input(f"Ne kadar {boz} bozdurmak istiyorsunuz: "))

print(f"1 {boz} = {result['rates'][boz]}")
print(f"{miktar} {boz} = {result['rates'][al] * miktar} {al}")
