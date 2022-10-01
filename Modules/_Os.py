import os
import datetime

result = os.name
print(result)

# os.chdir("/home/temetnosce/Desktop")
# os.mkdir("newdirectory")
# os.chdir("../..")
# os.makedirs("newdirectory/yeniklasör") # klasör altında klasör oluşturur. İki klasörü de oluşturur ama yeniklasörü içinde oluşturur.
# os.rename("newdirectory", "yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")  # klasörün içindeki klasörü siler.

# result = os.getcwd()    #dizin öğrenme
# print(result)

# result = os.listdir()
# print(result)
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

# result = os.stat("_Os.py")
# print(result)

# result = result.st_size/1024
# print(result)
# result = datetime.datetime.fromtimestamp(result.st_ctime)   # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)   # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)   # değiştirilme tarihi

# os.system("notepad.exe")  # notpepad uygulamasını çalıştırır.

# path

result = os.path.abspath("_Os.py") # dosyanının konumunu alıyosun (dosya ismi)
result = os.path.dirname("/home/temetnosce/PycharmProjects/BTK/Modules/_Os.py") # dosyanın tam yolunu veriyor (dizin ismi)
result = os.path.dirname(os.path.abspath("_Os.py"))
result = os.path.exists("/home/temetnosce/PycharmProjects/BTK/Modules/_Os.py") # result = os.path.exists("_Os.py")
result = os.path.exists("/home/temetnosce/PycharmProjects/BTK/Modules")
result = os.path.isdir("/home/temetnosce/PycharmProjects/BTK/Modules")
result = os.path.isfile("/home/temetnosce/PycharmProjects/BTK/Modules/_Os.py")
result = os.path.join("/home","deneme","deneme1") # Yeni dizin oluşturabilirsin böyle.
result = os.path.split("/home/deneme")
result = os.path.splitext("_Os.py") # uzantıyla ismi ayırır sonrasında değişim yapabilirsin falan.

print(result)