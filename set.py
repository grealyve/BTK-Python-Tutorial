fruits = { "banana", "orange", "apple", "mango"}

for i in fruits:
    print(i)

fruits.add("cherry")

fruits.remove("mango")
fruits.discard("apple")

fruits.pop() #rastgele eleman silinir

print(fruits)
fruits.update(["mango", "grape", "apple"]) #aynı elemanı eklemez

myList = [1,2,3,4,5,5,56,6,2]
print(myList)
print(set(myList)) #tekrarlanan elemanları çıkartır

#Listeler bir adrese bağlı olarak atanırlar
#
# a = b listesi yaptığında, b'de yaptığın bir değişiklik a'yı da etkiler. Birbirlerine bağlı bir ağda kayıt oldukları için.
# fakat bir a = 5 gibi bir value'de aynı şeyi yaptığında b'yi değiştirdiğin


