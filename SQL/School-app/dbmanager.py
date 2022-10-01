import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

# sınıf ekleme, ders ekleme, öğretmenlerle sınıf ve dersleri ilişkilendirme

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from student where id=%s"
        value = (id,)
        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane öğrenci silindi")
        except mysql.connector.Error as err:
            print("hata", err)

    def getClasses(self):
        sql = "select * from Class"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def getStudentByClassId(self,classid):
        sql = "select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender,ClassId) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} sayıda öğrenci eklendi")
        except mysql.connector.Error as err:
            print("hata", err)

    def editStudent(self, student: Student):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} sayıda öğrenci güncellendi")
        except mysql.connector.Error as err:
            print("hata", err)

    def addTeacher(self, teacher: Teacher):
        sql = "INSERT INTO Student(Branch, Name, Surname, Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane öğretmen eklendi")
        except mysql.connector.Error as err:
            print("hata", err)

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db silindi")

db = DbManager()

student = db.getStudentById(6)
student[0].name = "Ahmet"

db.editStudent(student[0])

# db.addStudent(student[0])

# print(student[0].name)

# students = db.getStudentByClassId(1)
# print(students[2].name)