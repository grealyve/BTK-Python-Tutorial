#for i in

numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

names = ["çınar", "sadık", "sena"]
for name in names:
    print(f"my name is {name}")

name = "Sadık Turan" #String de her karakteri bir liste gibi değerlendiriliyor. Her karakter bir dizi elemanı gibi davranıyor.
for n in name:
    print(n)

tuple = ((1,2),(1,3),(3,5),(5,7)) #tuple listesi gibi de yapabilirsin
for a,b in tuple:
    print(a)        #sadece ilk elemanı böyle yazdırabilirsin

d = {"k1":1, "k2":2, "k3":3}

'''for item in d.items():         #sadece d yazınca key bilgilerini verdi
    print(item) '''               # d.items() eleman gruplarını verir.

for key,value in d.items():
    print(key, value)
