'''isim = input("İsminiz: ")
yaş = int(input("Yaşınız: "))
egitim = input("Eğitim durumun: ")

if yaş >= 18:
    if (egitim == "uni" or egitim == "lise"):
        print("Ehliyet alabilirsin.")
    else:
        print("Ehliyet alamazsın eğitim durumun yetersiz.")
else:
    print("Ehliyet alamazsın yaşın tutmuyor.")

x = int(input("İlk yazılı: "))
y = int(input("İkinci yazılı: "))

result = (x + y) // 2

if 85 < result < 100:
    print(5)
elif 70 < result < 84:
    print(4)
elif 55 < result < 69:
    print(3)
elif 45 < result < 54:
    print(2)
elif 25 < result < 44:
    print(1)
else:
    print(0) '''

import datetime # from datetime import datetime yaparak direkt datetime modülünü çağırmadan fonksiyonu kullanabilirsin.

# dte = datetime.date(2000,12,27)
# ate = datetime.date(1998,12,27)
# print(dte-ate)

cikis = input("Aracınızın çıkış tarihi(2019/11/27): ")
cikis = cikis.split("/")
dte = datetime.datetime(int(cikis[0]),int(cikis[1]),int(cikis[2]))
now = datetime.datetime.now()
fark = now - dte
farkv = fark.days

if farkv <= 365:
    print("1.Servis.")
elif farkv > 365 and  farkv < 365*2:
    print("2.Servis")
elif farkv > 365*2 and farkv < 365*3:
    print("3.servis")
else:
    print("Hatalı giriş.")