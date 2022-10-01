'''x = 0

while x <= 100:
    if x % 2==0:
        print(f"sayı çift: {x}")
    else:
        print(f"sayı tek: {x}")
    x += 1
print("bitti...")

name = "" #False
while not name.strip():
    name = input("isminizi giriniz: ")

print(f"Merhaba, {name}") '''

sayilar = [1,3,5,7,9,12,19,21]

# n = 0
#
# while n < len(sayilar):
#     print(sayilar[n])
#     n += 1

# baslangic = int(input("İlk sayı: "))
# son = int(input("Son sayı: "))
#
# i = baslangic
# while i < son:
#     if i % 2 == 1:
#         print(i)
#     i += 1

# x= 100
# while x > 0:
#     print(x)
#     x -= 1

# liste1 = []
# i = 0
#
# while i<5:
#     sayi = int(input("sayı : "))
#     liste1.append(sayi)
#     i+= 1
# liste1.sort()
# print(liste1)

'''urunler = []
sayi = int(input("sayı: "))
i = 0
while(i<sayi):
    name = input("ürün ismi: ")
    price = input("ürünün fiyatı: ")
    urunler.append({
        "name" : name,
        "price": price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]}, ürün fiyatı: {urun["price"]}')'''

# break and continue    #break döngüyü kırar
name = "Sadık Turan"
for letter in name:
    if letter == "ı":
        continue        #continue sadece o anki döngü turunu iptal eder ve kaldığı yerden devam eder.
    print(letter)

x = 0
while x < 5:
    x += 1
    if x == 2:
        continue        #döngüyü iptal ettiği için başa döner ve x=2'de takılı kalır. Bu yüzden x+=1 i önce yazmak gerek.
    print(x)

# 1- 100 e kadar tek sayıların toplamı

x = 0
result = 0
while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x

print(f"toplam {result}")