#list'e benziyor ama köşeli parantez yerine normal parantez kullanabilirsin.

tuple = (1, "iki", 3)  #parantezsiz de yazılır

print(type(tuple))

print(tuple[2])

print(len(tuple))

#tuple'da list'deki gibi bir değerin üzerine atama yapılamaz yani değiştiremezsin içindekini list[0] = "Ali" gibi olmaz

names = ("ali", "ayşe", "damla") + tuple
print(names)