'''sayilar = [1, 3, 5, 7, 8, 12, 19, 21]
l1 = []
for i in sayilar:
    if i % 3 == 0:
        l1.append(i)
print(l1)

n = 0
for x in sayilar:
    n += i
print(n)

for y in sayilar:
    if y % 2 == 1:
        y = y ** 2
    print(y)


sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]
bej = []
for i in sehirler:
    if len(i) <= 5:
        bej.append(i)
print(bej) '''

urunler = [
    {"name": "samsung S6", "price": 3000},
    {"name": "samsung S7", "price": 4000},
    {"name": "samsung S8", "price": 5000},
    {"name": "samsung S9", "price": 6000},
    {"name": "samsung S10", "price": 7000}
]
# toplam = 0
# for urun in urunler:
#     fiyat = int(urun["price"])
#     toplam += fiyat
# print(toplam)

for urun in urunler:
    if int(urun["price"]) <= 5000:
        print(urun["name"])