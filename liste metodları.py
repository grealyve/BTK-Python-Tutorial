numbers = [1, 4, 10, 15, 8, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
numbers[1] = 40
numbers.append(39)          #en sona parantez içindeki değeri ekler
numbers.insert(6, 78)       #6.indexte kendine yer açar ve 78 değerini girer
numbers.pop(0)              #içine index girmezsen en sondaki değeri siler
numbers.remove(40)          #içine yazdığın değeri siler
numbers.sort()              #sırasına göre sıralanır
letters.sort()
numbers.reverse()           #listeyi ters çevirir
print(numbers.count(10))    #liste içinde parantez içindeki değerden kaç tane var ona bakabilirsin
print(letters.count("a"))
letters.clear()             #bütün elemanları siler


print(numbers)

names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

names.append("Cenk")
print(names)
names.insert(0, "Sena")         #En sona insert ile eklemek için names.insert(len(names), "Sena")
print(names)
#names.remove("Deniz")
x = names.index("Deniz")
print(x)
y = "Ali" in names
print(y)
names.reverse()
names.sort()
years.sort()
str1 = "Chavrolet,Dacia"
str1 = str1.split(",")
print(str1)
z = max(years)
print(z)
z = min(years)
print(z)
print(years.count(1998))
years.clear()

# marka = input("3 tane marka ismi yaz:")
# marka = marka.split()
# print(marka)

markalar = []

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

print(markalar)