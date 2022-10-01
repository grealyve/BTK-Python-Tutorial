liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1- Sayısal değerleri bul.

# for i in liste:
#     try:
#         result = int(i)
#         print(result)
#     except Exception as e:
#         print(e)
#         continue

# 2- "q" girmedikçe her input sayı

# while True:
#     x = input("Sayı giriniz: ")
#     if x == "q":
#         break
#     else:
#         try:
#             float(x)
#             print(x)
#         except Exception as e:
#             print(e)

# 3- Türkçe karakter hatası:

# def checkPassword(pwd):
#     import  re
#     if re.search("[ğşİöçĞŞıÖÇ]", pwd):
#         raise Exception("Parola türkçe karakter içermemeli!")
#     else:
#         print("Geçerli parola")
#
#
# try:
#     checkPassword("alini")
# except Exception as e:
#     print(e)
# finally:
#     print("Dönüşüm tamamlandı!")

#2.seçenek###########################################

# turkce_karakterler = "şçğüiıİ"
#
# parola = input("parola: ")
#
# for i in parola:
#     if i in turkce_karakterler:
#         raise TypeError("Parola türkçe karakter içeremez.")
#     else:
#         pass
#     print("Geçerli parola")


# 4- Faktöriyel

def fack(x):
    x = int(x)
    if x < 0:
        raise ValueError("Negatif değer")

    n = 1
    for i in range(1, x+1):
        n *= i
    return n

print(fack(6))
for x in [5,10,20,-3,"10a"]:
    try:
        y = print(fack(x))
    except ValueError as e:
        print(e)
        continue

    print(y)