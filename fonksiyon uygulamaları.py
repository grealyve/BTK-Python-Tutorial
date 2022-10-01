# def word(kelime, sayi):
#     for i in range(sayi):
#         print(kelime)
#
# word("alii", 10)

#HER PARAMETREYİ BİR LİSTEYE ÇEVİREN FONKSİYON
# def cevirBaba(*parametre):
#     list = []
#     for param in parametre:
#         list.append(param)
#     return list
#
# print(cevirBaba(3, "ali", 4.0329123, "Veli"))

def asallar(a, b):
    lis = []
    x = 2
    while x < b:
        if a < x:
            for i in range(2,x):
                if x % i == 0:
                    break
            else:
                lis.append(x)
        x += 1
    return lis

print(asallar(10,50))

# def asallar(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
#
# sayi1 = int(input("sayı 1: "))
# sayi2 = int(input("sayı 2: "))
#
# print(asallar(sayi1, sayi2))

# def bolenler(x):
#     for i in range(1,x+1):
#         if x % i == 0:
#             print(i)
#
# bolenler(50)