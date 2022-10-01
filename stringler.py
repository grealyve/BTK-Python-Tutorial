website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

print(len(course))
print(website[7:10])
print(website[-3:])
print(course[0:16], course[-15:])
print(course[::-1]) # Tersten yazdırma

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'
print(f"Benim adım {name} {surname} yaşım {age} ve mesleğim {job}.")

print("abc"*5)

result = 200 / 700
print('the result is {r:2.4}'.format(r=result)) # 2, "is"den sonra kaç boşluk olacağını; 4 ise kaç basamağı yazılacağını belirtir.