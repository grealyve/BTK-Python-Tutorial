'''
a = float(input("Sayı: "))
if (a > 0) and (a < 100):
    print("Sayı 0-100 aralığında")
else:
    print("Sayı 0-100 aralığında değil.")

sayi = int(input("Sayı: "))
if (sayi>0) :
    if (sayi%2 == 0):
        print("Girilen sayı pozitif çift sayıdır")
    else:
        print("Girilen sayı pozitif ancak tek")
else:
    print("Sayı negatif")

email = "ali"
password = "abc123"

girilenEmail = input("email: ")
girilenpassword = input("password: ")

if girilenEmail == email:
    if girilenpassword == password:
        print("Giriş başarılı")
    else:
        print("Eposta doğru fakat şifre yanlış")
elif (girilenpassword == password) and (girilenEmail != email):
    print("Şifre doru ama eposta yanlış")
else:
    print("Eposta yanlış.")

a = int(input("Sayı: "))
b = int(input("Sayı: "))
c = int(input("Sayı: "))

if (a > b) and (a > c):
    print("a en büyük sayı")
elif (b > a) and (b > c):
    print("b en büyük sayı")
else:
    print("c en büyük sayı")
###########
vize1 = int(input("Vize1: "))
vize2 = int(input("Vize2: "))
final = int(input("Final: "))
ort = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

if (ort >= 50):
    if (final > 50):
        print("Geçtin")
    else:
        print("Ortalaman tuttu ama finalden düşük almışsın.")
elif (final > 70):
    print("Finalden 70 üstü aldığın için geçtin")
else:
    print("Kaldın")

if (ort >= 50):
    print("Geçtin")
else:
    if (final >= 70):
        print("Finalden 70 üstü aldığın için geçtin")
    else:
        print("Başarısız")
'''
name = input("adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("boyunuz: "))

index = (kg) / (hg ** 2)
zayif = (index > 0) and (index < 18.4)
normal = (index > 18.5) and (index < 24.9)
Kilolu = (index > 25.0) and (index < 29.9)
obez = (index > 30) and (index < 49.9)

# print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif} ")
# print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal} ")
# print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen fazlaKilolu: {fazlaKilolu} ")
# print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez} ")
print(index)
if zayif:
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf")
elif normal:
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal")
elif Kilolu:
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen Kilolu")
elif obez:
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez")
else:
    print("Bilgileriniz Yanlış!")