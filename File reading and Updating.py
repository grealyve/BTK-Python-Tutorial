'''
with open("newfile.txt", "r", encoding="utf-8") as file:
    # file.close() yapmaya gerek kalmıyor.
    content = file.read(10)
    print(content)
    file.seek(0)            # imleci istediğin konuma gönderebilirsin.
    print(file.tell())      # imlecin hangi konumda olduğunu söyler.
    content2 = file.read()
    print(content2) '''

# Updating

# with open("newfile.txt", "r+", encoding="utf-8") as file:  # "r+" hem okuma hem yazma demek
#     file.seek(20)
#     print(file.write("deneme"))
#
# with open("newfile.txt", "r+", encoding="utf-8") as file:  # "r+" hem okuma hem yazma demek
#     print(file.read())

# ******** Sayfa Sonunda Güncelleme ********

# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nEmel Turan")

# ******** Sayfa Başında Güncelleme *********

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe Turan\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)

# ********* Sayfa Ortasında Güncelleme ********

with open("newfile.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(1,"Yılmaz Aygün\n")
    file.seek(0)
    # for i in liste:
    #     file.write(i)
    file.writelines(liste)

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())