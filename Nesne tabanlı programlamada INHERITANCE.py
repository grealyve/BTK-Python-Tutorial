# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, eat(), run()
# Student(Person), Teacher(Person) --> Person'ın özelliklerini de barındırması demek kalıtım.Ama Student classındakileri Person bulundurmaz

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")
    def who_am_I(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)         #Bunu yazmazsan Person, Student'ı ezer ve kullanılamaz class
        self.studentNumber = number
        print("Student Created")

    # override
    def who_am_I(self):
        print("I am a student")

class Teacher(Person):
    def __init__(self,fname,lname, branch):
        super().__init__(fname, lname)              # super().__init__ de olur
        self.branch = branch

    def who_am_I(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Ali", "Yılmaz")
s1 = Student("Çınar", "Turan", 1242)
t1 = Teacher("Serkan", "Yılmaz", "Math")

t1.who_am_I()
print(p1.firstName + " " + p1.lastName)
print(f"{s1.firstName} {s1.lastName} {s1.studentNumber}")
s1.who_am_I()
s1.eat()

# Special Methods

mylist = [1,2,3]
# myString = "my string"
#
# print(len(mylist))
# print(len(myString))

class Movie():
    def __init__(self,title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("film objesi silindi")


m = Movie("Ahlat ağacı", "Nuri Bilge Ceylan", 180)

# print(str(mylist))
print(str(m))
print(len(mylist))
print(len(m))

# del m      bunu yazmasak bile metodu var olduğu için belli süre sonra siliniyor kendi
# print(m)

