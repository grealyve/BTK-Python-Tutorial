# def gcd(x, y):
#     while y != 0:
#         x, y = y, x % y
#     return x
#
# def coprime(a, b):
#     return gcd(a, b) == True
#
# print(coprime(21,22)) #Should be true
# print(coprime(14,28)) #Should be false

def aralarindasal(x, y):
    l = []
    for i in range(2,x+1):
        if x % i == 0:
            l.append(i)
    print(l)
    for a in l:
        if y % a == 0:
            print("Aralarında asal değiller.")
            break
    else:
        print("Aralarında asaldır.")


aralarindasal(17, 18)


# x 'i bölenleri ayır sonra y'de dene.