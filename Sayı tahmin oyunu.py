'''import random

x = random.randrange(1,100)
print(x)
hak = int(input("Hak sayınız: "))
sayac = 0
print(f"Geçerli hak sayınız: {hak}")

while hak > 0:
    tahmin = int(input("Tahmininiz: "))
    sayac += 1
    hak -= 1
    if tahmin < x:
        print("Yukarı!")
    elif x == tahmin:
        print("Doğru bildiniz!")
        print(f"Puanınız : {hak * (100/hak)} ")
        print(f"Tebrikler {sayac}, defada bildiniz.")
        break
    else:
        print("Aşağı!")
    if hak == 0:
        print(f"Puanınız 0. Sayı : {x} idi.")
        break '''

sayi = int(input("Sayı: "))
asalmi = True

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")