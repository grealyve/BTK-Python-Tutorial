# Object Oriented Programming (OOP)

# class => Person (name,surname,birthday, calculateAge())
# instance (object)
#Burada oluşturduğun bir liste, list classından kopyalanıp oluşturulmuş bir instance yani nesnedir.
#class daha önceden oluşturulmuş, içinde belli başlı metotları bulundurur.
lst = [1,2,3]

result = type(lst)
lst.append(3)       # gibi metotları instance üzerinden kullanabilirsin
print(result)

# instance (object)

# Class üretme ve metodlarını üretme

class Person:
                    #pass yer tutucu olarak hata vermeden kullanılıabilir bu class
    # class attributes
    address = "no information"

    # constructor(yapıcı metod)
    def __init__(self, name, year):              #self p1 ve p2 gibi classtan türetilen objeleri temsil eder.
        # object attributes                      #self yerine ali de yazabilirsin
        self.name = name
        self.year = year
        print("init metodu çalıştı")


    #methods
    def intro(self):
            print("Hello There I am " + self.name)

    def calculateAge(self):
        return 2021 - self.year

p1 = Person("ali", 1990)
p2 = Person(name = "yağmur",year = 1995)        #daha okunuaklı olur
#updating
p1.name = "ahmet"
p1.address = "kocaeli"
#accessing object attributes
print(f"name: {p1.name}, year: {p1.year}, adres: {p1.address}")
print(p1)
print(type(p2))
print(p1 == p2)

p1.intro()
print(f"yaşım: {p1.calculateAge()}")
#########################################################
class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self,):
        return 2 * self.pi * self.yaricap
    def alan(self):
        return self.pi * (self.yaricap**2)

c1 = Circle()
c2 = Circle(5)

print(f"c1: alan = {c1.alan()}, çevre = {c1.cevre_hesapla()}")
print(f"c1: alan = {c2.alan()}, çevre = {c2.cevre_hesapla()}")
