# my_list = ["Ali", 2.6, True]
# print(my_list)
#
# list1 = ["one", "two", "three"]
# list2 = ["four", "five", "six"]
#
# numbers = list1 + list2
# print(numbers)
# print(len(numbers))
#
# userA = ["Ali", 32]
# userB = ["Çıldırdülfür", 22]
#
# users = [userA ,userB]
# print(users)
# print(users[1][0])

list1 = ["Bmw", "Mercedes","Opel", "Mazda"]
print(len(list1))
print(list1[0], list1[3])
list1[-1] = "Toyota" #Listenin içindeki bir değeri değiştirme
print(list1)
index = list1.index("Mercedes") #Mercedes'i listenin içinde bulma
print(index)
result = "Mercedes" in list1 #Mercedes'i listenin içinde bulma (2.YOL)
print(result)
result = list1[:3]
print(result)
list1[-2] = "Toyota"             #Son iki değeri değiştirme
list1[-1] = "Renault"            # list1[-2:] = ["Toyota", "Renault"]
print(list1)
list1[4:] = ["Audi", "Nissan"]  #list1 + ["Audi", "Nissan"]
print(list1)
list1.remove("Nissan")          # del list1[-1]
print(list1)
list1.reverse()                 # list1[::-1]
print(list1)
studentA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB = ["Sena", "Turan", 1999, [80, 80, 80]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]
print(studentA + studentB + studentC)

result = f"{studentC[0]} {studentC[1]} {2021-studentC[2]} yaşında ve not ortalaması {(studentC[3][0] + studentC[3][1] + studentC[3][2])/3}"
print(result)