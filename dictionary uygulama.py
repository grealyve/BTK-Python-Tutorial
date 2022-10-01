# i = {
#     input("Okul numaranı gir: "): {
#         "ad": input("Adını gir: "),
#         "soyad": input("Soyadını gir: "),
#         "telefon": input("Telefon numaranı gir: ")
#     },
#     input("Okul numaranı gir: "): {
#         "ad": input("Adını gir: "),
#         "soyad": input("Soyadını gir: "),
#         "telefon": input("Telefon numaranı gir: ")
#     },
#     input("Okul numaranı gir: "): {
#         "ad": input("Adını gir: "),
#         "soyad": input("Soyadını gir: "),
#         "telefon": input("Telefon numaranı gir: ")
#     },
# }
#
# print(i)
#
# print(i[input("Okul numaranı gir: ")])

#*********************************************************************

# ogrenciler = {}
#
# number = input("Öğrenci numarası: ")
# name = input("öğrenci adı: ")
# surname = input("öğrenci soyadı: ")
# phone = input("öğrenci telefon: ")

# ogrenciler[number] = {
#     "ad": name,
#     "soyad": surname,
#     "telefon": phone
# }

#**********************************************************************

# i.update({
#     number: {
#         "ad": name,
#         "soyad": surname,
#         "telefon": phone
#     }
# })

ogrenciler = {}

for i in range(3):
    ogrenciler.update({
        input("Öğrenci numarası: "): {
            "ad": input("öğrenci adı: "),
            "soyad": input("öğrenci soyadı: "),
            "telefon": input("öğrenci telefon: ")
         }
     })

print(ogrenciler)