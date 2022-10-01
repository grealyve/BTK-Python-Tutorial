'''a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = 1

while n*n < a:
    n += 1
while n*n <= b:
    print(n*n)
    n += 1 '''

#round 2

'''a = input("Enter a: ")
a = int(a)
b = input("Enter b: ")
b = int(b)
if a < b:
    smaller = a
    larger = b
else:
    smaller = b
    larger = a
n = 1
while (smaller*n)%larger != 0:
    n += 1
print(smaller*n) '''

'''def tekSayi(x):
    while x < 101:
        if x % 2 == 1:
            print(x)
            x += 1
        else:
            x += 1

tekSayi(1) '''

'''x = float(input("Fiyat: "))
a = x * 118/100
print(a)'''

'''def faktoriel (x):
    n = 1
    for i in range(1, x+1):
        n = n * i
    print(n)

faktoriel(5) '''



'''x = float(input("Fahrenheit: "))
cel = (x - 32) / 1.8
print(cel) 
'^++%%%!'^!'^!'^!'^!'^!'!'^!'
import math

abi1 = int(input("a= "))
abi2 = int(input("b= "))
abi3 = int(input("c= "))


delta = (abi2)**2 - 4 * abi1 * abi3

kok1 = (-(abi2) + math.sqrt(delta)) / (2 * abi1)
kok2 = (-(abi2) - math.sqrt(delta)) / (2 * abi1)
print(kok1)
print(kok2) 

x = int(input("Su: "))

if x < 0:
    print("Katı halde")
elif x == 0:
    print("Hem katı hem sıvı")
elif x == 100:
    print("Hem sıvı hem gaz")
else:
    print("Gaz")

calisan = {
    "ali": {
        "age" : int(input("Çalıştığı saat: ")),
        "phone" : float(input("Parayı tükür: "))
    },
}

print((calisan["ali"]["age"]) * (calisan["ali"]["phone"])) 
##
import math
a = float(input("Kenar uzunluğu: "))
c = float(input("Kenar uzunluğu: "))
b = float(input("Kenar uzunluğu: "))

if math.fabs(a + b) > c > math.fabs(b - c):
    if (a == b == c):
        print("Eşkenar")
        print(a + b + c)
    elif (a == b) or (b == c) or (a == c):
        print("İkizkenar")
        print(a + b + c)
    else:
        print("Çeşitkenar")
        print(a + b + c)
else:
    print("Üçgen Çizilemez")

while True:
    l = 0
    a = []
    for i in range(7, 25):
        if (i % 2 == 1):
            l += i
            a.append(i)
    print(l)
    print(l / len(a))
    break

def sayi(x):
    l = []
    for i in range(0,x):
        a= int(input("Sayı giriniz: "))
        l.append(a)
    print(max(l))
    print(min(l))

sayi(10) 
##
while True:
    a = int(input("Sayı: "))
    if 10 < a < 15:
        break 

#####
n = 0
for i in range(0,26):
    a = i * i
    n += a
print(n) 

aylar = {1 : "Ocak", 2: "Şubat", 3: "Mart", 4:"Nisan"}

print(aylar[int(input("Sayı: "))]) 
print("1-toplama \n2-çıkartma \n3-çarpma \n4-bölme")
a = int(input("Sayı: "))
b = int(input("Sayı: "))

choice = int(input("1-toplama, 2-çıkartma, 3-çarpma, 4-bölme: "))
if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a // b)
else:
    print("Hatalı giriş: ") 

x = int(input("Mesafe: "))
print(f"Araç, {x} km'yi", x//60, "saatte gider.")

#-Write a program that inputs one five-digit number, separates the number into its individual digits and prints
#the digits separated from one another by three spaces each. [Hint: Use combinations of integer division and the
#remainder operation.] For example, if the user types in 42139, the program should print
sayi = input("Beş basamaklı sayı gir: ")
n = 0
for i in range(5):
    print(sayi[n:n+1])
    n += 1
##########
sayi = input("Sayı giriniz: ")
l1 = []
for i in sayi:
    l1.append(i)

if (l1[0] == l1[4]) and (l1[1] == l1[3]):
    print("It's a palindrome number.")
else:
    print("It's not a palindrome number.")'''

sayi = input("Beş basamaklı sayı gir: ")
l1 = []
for i in sayi:
    l1.append(i)

print(f"{l1[0]}\t{l1[1]}\t{l1[2]}\t{l1[3]}\t{l1[4]}")


