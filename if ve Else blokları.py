#if 3>2:                         #if'in yanına yazdığın değerin True ya da False değerini üretmesi gerek.
#    print("Hoş geldiniz")


# username = "sadikturan"
# password = "1234"
#
# isLoggedin = (username == "sadikturan") and (password == "1234")
#
# if isLoggedin:
#     print(2121)
# else:
#     print("username ya da parola yanlis")

# username = "sadikturan"
# password = "1234"
#
# if (username == "sadikturan"):
#     if (password == "1234"):
#         print("Hoş geldin")
#     else:
#         print("parola yanlış")
# else:
#     print("username yanlis")

# inputtan gelen değerler str olarak algılanır.
x = 20
y = 20

if x > y:
    print("x y den büyük")
elif x == y:
    print("x y eşit")
else:
    print("y x den büyük")

num = int(input("sayı: "))

if num > 0:
    print("sayı pozitif")
elif num < 0:
    print("sayı negatif")
else:
    print("sayı sıfır")