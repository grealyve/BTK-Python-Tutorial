#range while içinde de kullanılır.

# for item in range(5,10,2):
#     print(item)

print(list(range(5,100,10)))

#enumerate

# index = 0
# greeting = "Hello There"
#
# for letter in greeting:
#     print(f"index: {index} letter: {greeting[index]}")    #letter: {letter} yerine
#     index += 1

greeting = "Hello"

for item in enumerate(greeting):            # enumarate = numaralandırma
    print(item)                             # herhangi bir iteratoru ilk elemandan başlayarak zip gibi numaralandırır.
                                            # kaçtan başlamasını istiyorsan virgülden sonra yazabilirsin.
#zip

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

print(list(zip(list1, list2)))

for item in zip(list1, list2):
    print(item)

for a,b in zip(list1, list2):
    print(a)