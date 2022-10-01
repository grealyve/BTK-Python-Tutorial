# def ebob(x, y):
#     l1 = []
#     l2 = []
#     for i in range(2,x+1):
#          if x % i == 0:
#              l1.append(i)
#
#     for z in range(2,y+1):
#          if y % z == 0:
#              l2.append(z)
#
#     print(l1)
#     print(l2)
#     l3 = []
#     for a in l1:
#         if a in l2:
#             l3.append(a)
#     return max(l3)
#
# print(ebob(60, 24))

def ekok(x, y):
    if x > y:
        for i in range(1, x+1):
            if ((y * i) % x) == 0:
                print(y * i)
                break
    else:
        for a in range(1, y+1):
            if ((x * a) % y) == 0:
                print(x * a)
                break

ekok(3, 5)