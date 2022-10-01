# Yöntem 2
# import math as islem

# value = dir(math)
#
# print(value)
# value = help(math)
# value = math.sqrt(49)
# print(value)
# value = math.factorial(5)
# print(value)
# value = math.floor(5.9)
# print(value)
# value = math.ceil(5.9)
# print(value)

# value = islem.factorial(5)

# Yöntem 2
#from math import *      #Belirli fonk. çağırabilirsin ya da * ile hepsini
import random


def sqrt(x):
    print(("x: "+ str(x)))      #en son hangi fonksiyon tanımlandıysa onu kullanır

from math import factorial, sqrt

value = factorial(5)
print(value)

value = sqrt(9)
print(value)

import random

result = random.random() # 0.0-1.0
result = random.uniform(10,100)
print(result)
result = random.randint(1,1000)

names = ["ali", "yağmur", "deniz", "at", "ahmet"]
# result = names[random.randint(0,len(names)-1)]
print(result)
result = random.choice(names)
print(result)
greeting = "Hello There!"
result = random.choice(greeting)
print(result)

liste = list(range(10))
random.shuffle(liste)
result = liste
print(result)

liste = range(100)
result = random.sample(liste, 3)
print(result)
result = random.sample(names, 2)
print(result)