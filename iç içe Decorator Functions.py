# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper
#
# @my_decorator           # sayhello = my_decorator(sayhello)
# def sayhello(name):
#     print("hello", name)
#
# sayhello("ali")
import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " + func.__name__+" "+ str(finish - start) + " saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2,3)
faktoriyel(4)
