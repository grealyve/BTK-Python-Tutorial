'''def changeName(n):
    n = "ada"

name = "yiğit"

changeName(name)

def change(n):
    n[0] = "istanbul"

sehirler = ["ankara", "izmir"]
n = sehirler[:]    #slicing

n[0] = "istanbul"

change(sehirler[:])
print(sehirler)
print(n)    '''
#
# def add(a,b,c=0):       #tek tek parametreleri belirtmek yerine * koyup yapabilirsin(tuple olur ama)
#     return sum((a,b,c))
#
# print(add(10, 20))

# def add(*params):
#     print(params)
#     print(params[2])
#     return sum((params))
#
# print(add(10,20,30,100,30,20,14))

def displayUser(**args):        #dictionary olmasını istediğimiz için 2 tane * koyudk
    for key, value in args.items():
        print("{} is {}".format(key, value))

displayUser(name= "Çınar", age = 2, city = "istanbul")
displayUser(name= "ALİİİİİ", age = 15, city = "istanbul", phone = "21312543")

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1 = "value1", key2 = "value2")