# Dosya açmak ve oluşturmak için open() fonksiyonu kullanlılır.
# Kullanımı : open(dosya_adi, dosya_erişme_modu)    # mod derken "r" gibi komut.
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur.
#               ** Daha önce olan bilgiler, sonradan eklenen bilgiler tarafından silinir.
#               ** Dosya içeriğini siler ve yeniden ekleme yaparsan yapar.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
#               ** Daha önce olan verinin üzerine ekleme yapar.
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. Varsayılan. Dosya konumda yoksa hata verir.

# "w"

# file = open("/home/temetnosce/Desktop/newfile.txt", "w")
# print(file)

# file = open("newfile.txt", "w", encoding="utf-8")
# print(result)

# file.write("Sadık Turan")
# file.close()

# "a"

# file = open("newfile.txt", "a", encoding="utf-8")
# file.write("\nSadık Turan")
# file.close()

# "x"
#
# file = open("newfile2.txt", "x", encoding="utf-8")

# "r"

file = open("newfile.txt", "r", encoding="utf-8")      # "r" yazmasan bile default olarak orada var

# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı")
#     file.close()

# for döngüsü

# for i in file:
#     print(i, end="")        # print işlemi yaptıktan sonra 1 satır boşluk bırakır

# *********** read() fonksiyonu ********************** for döngüsü yerine kullanabilirsin

# content1 = file.read()
#
# print("içerik 1")
# print(content1)
#
# content2 = file.read()    # 1 kere okuduktan sonra dosya kapanmadığı için imleç en sonda kalır.
#                           # ve oradan okumaya devam etmeye çalışır.
# print("içerik 2")
# print(content2)

# content = file.read(5)   # sayı, byte'ı ifade eder, her karakter 1 byte olarak hesaplanır
# content = file.read(3)
# content = file.read(3)
# print(content)

# ************  readline() fonksiyonu****************
# her fonksiyonda 1 satır okur.
# print(file.readline(), end="")             # content = file.readline()
# print(file.readline(), end="")
# print(file.readline())
# print(file.readline())


# *************  readlines()  *********************
liste = file.readlines()        # her bilgiyi listenin elemanı olarak gösterir
print(liste)
print(liste[0])

file.close()

