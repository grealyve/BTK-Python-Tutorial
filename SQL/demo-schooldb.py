import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "schooldb"
)

class Student:
    mydb = mydb                 # Bu ikisine statik değerler deniyor.
    mycursor = mydb.cursor()

    def __init__(self,id,studentNumber, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql, value)    # Statik değerlere class içerisinden böyle ulaşırsın.

        try:
            Student.mydb.commit()
            print(f"{Student.mycursor.rowcount} sayıda öğrenci eklendi")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.mydb.close()

    @staticmethod
    def saveStudents(students): # Dışarıdan öge alacağımız için classın içindeki isntance ögeler yani self.name gibileri(instance)
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql, values)

        try:
            Student.mydb.commit()
            print(f"{Student.mycursor.rowcount} sayıda öğrenci eklendi")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.mydb.close()
    
    @staticmethod
    def studentInfo():
        sql = "Select * From Student where gender='K' order by name,surname"

        Student.mycursor.execute(sql)
        try:
            result = Student.mycursor.fetchall()
            for students in result:
                print(students)
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.mydb.close()

    @staticmethod
    def searchStudentById(id):
        sql = "Select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("hata", err)

    def updateStudent(self):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.mydb.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("Hata: ", err)

    @staticmethod
    def searchByGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("hata", err)

    @staticmethod
    def updateStudent(liste):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)
        try:
            Student.mydb.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("Hata: ", err)


students = Student.searchByGender("E")
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = "Mr " + std[2]
    liste.append(std)

Student.updateStudent(liste)

# student = Student.searchStudentById(6)

# student.name = "Ahmet"
# student.surname = "Çınar"

# student.updateStudent()

# print(obj)

# Student.studentInfo()

# ahmet = Student("202","ahmet","yılmaz",datetime(2005, 5, 31),"E")
# ahmet.saveStudent()

# values = [
#     ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
#     ("302","Ali","Can",datetime(2005, 5, 31),"E"),
#     ("303","Canan","Tan",datetime(2004, 8, 21),"K"),
#     ("304","Ayşe","Taner",datetime(2005, 9, 18),"K"),
#     ("305","Bahadır","Toksöz",datetime(2006, 2, 27),"E"),
#     ("306","Ali","Cenk",datetime(2003, 8, 13),"E")
# ]

# mycursor.executemany(sql, values)

# Student.saveStudents(values)


#######################################################################
# def searchStudent():
        # mycursor = mydb.cursor()

        # mycursor.execute("Select * From Student")
        # mycursor.execute("Select name,surname From Student")
        # mycursor.execute("Select name,surname From Student Where gender='K'")
        # mycursor.execute("Select * From Student Where birthdate LIKE '%2003%' and name='Ali'")       Where YEAR(birthdate) = 2003
        # mycursor.execute("Select * From Student Where name LIKE '%an%' or surname LIKE '%an%'")
        # mycursor.execute("Select COUNT(*) From Student Where gender='E'")
        # mycursor.execute("Select * From Student Order By Where gender='K'")


        # result = mycursor.fetchall()

        # for students in result:
            # print(f"id: {students[1]},name: {students[2]} {students[3]}, gender: {students[5]}")
            # print(f"name: {students[0]}, surname: {students[1]}")
            # print(students)