# def greeting(name):
#     print("hello", name)

# print(greeting("ali"))
# print(greeting)       # bellekteki adresini gösteriyor

# sayHello = greeting     # Atama işlemi datanın adresine eşitlemiş oluyorsun.
# print(sayHello)
# print(greeting)

# print(greeting("ali"))  = print(sayHello("ali")) aynı şey olmuş oluyor.
############## ENCAPSULATION #########################
#
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)
#
# outer(10)
# inner_increment(10)   FONKSİYONUN İÇİNDE OLDUĞU İÇİN TANIMLI OLARAK GÖRMÜYOR.

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero")

    def inner_factorial(number):
        if number <= 1:
            return 1
        print(number)
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

try:
    print(factorial(5))
except Exception as ex:
    print(ex)