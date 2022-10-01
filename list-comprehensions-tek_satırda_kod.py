numbers = []
for x in range(10):
    numbers.append(x)

print(numbers)

numbers = [x for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10)]

numbers = [x*x for x in range(10) if x%3==0] #sadece 3'e bölünenleri verir, else yazmak için en başa yazman gerekir
print(numbers)

myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

years = [1983, 1999, 2008, 1965, 1986]
ages = [2022-year for year in years]    #for döngüsü gerekmeden tek satırda matematiksel işlem
print(ages)

results = [x if x%3==0 else "TEK" for x in range(1,10)] #çift sayıysa sayıyı yazar, tek ise Tek yazar.
print(results)

numbers = [(x,y) for x in range(3) for y in range(3)] #iç içe döngü
print(numbers)