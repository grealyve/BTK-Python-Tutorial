message = "Hello There. My name is GreaLyve "

message = message.upper()  #bütün harfleri büyütür.
message = message.lower()  #bütün harfleri küçük yazar.
message = message.capitalize() #Sadece cümlenin ilk harfini büyük yazar
message = message.title() #her kelimenin ilk harfini büyük yazar.
message = message.strip() #cümlenin başındaki ve sonundaki boşlukları siler.
message = message.split(".") #her kelimeyi ayırır ve diziye dönüşür. İçine nokta yazarsan cümleyi noktadan itibaren ayırır.
message =" ".join(message) #arada boşluk bırakarak splitle ayırdığımız kelimeleri birleştirdi.
index = message.find("GreaLyve") #cümlede, kelimenin ilk harfinin kaçıncı indexte olduğunu bulur. -1 değeri cümlenin içinde yok demektir.
isFound = message.startswith("H") #cümlenin hangi harfle başlayıp başlamadığını .endswith hali de vardır.
message = message.replace(" ", "32").replace("My", "Aliii") #cümle içinde ilk tırnağın içine yazılan karakteri arar ve yerine 2.tırnaktaki yazdığını yapıştırır. şeklinde devam ettirebilirsin
message = message.center(50, "*") #Mesajı 50 karakterlik bir boşluğun içie alır ve yıldızla kaplar


print(isFound)
print(message)

website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

a = " Hello World ".strip()
print(a)
a=website.lstrip(":/htp")
print(a)
a = website.rstrip("htp:/.w.com")
print(a)
a = course.upper()
print(a)
a = website.count("a")
print(a)
a = website.startswith("www")
print(a)
a = website.endswith("com")
print(a)
a = website.find(".com")
a = website.find(".com",0,10) # 0 ve 10 arasına bakar
print(a)
a = "Contents".ljust(50, "*") # Contents***********************
print(a)
a = course.replace(" ", "-",5)
print(a)
a= course.split()
print(a)