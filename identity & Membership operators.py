# Identity Operator : is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x is y)       # is operatörü aynı adresin tutup tutmadığına bakar
print(x is z)       # içindeki değerlere değil.

k = [1, 2, 3]
l = [2, 4]

del k[2]
l[1] = 1
l.reverse()

print(k==l)
print(k is l)
print(k is not l)
# Membership operator : in

x = ["apple", "banana"]
print("banana" in x)

name = "Çınar"
print("a" in name)
print("a" not in name)