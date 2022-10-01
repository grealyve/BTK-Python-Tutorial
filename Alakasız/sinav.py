# def uniteLists(aList, bList):
#     newList = aList + bList
#     newList = list(set(newList))
#     return newList
#
# x = [4,4,4,4,3,2,1,9,9]
# y = [2,2,2,1,1,4,4,4,4,9,8,7]
# print(uniteLists(x,y))
#

# def uniteLists(aList, bList):
#     l = []
#     for i in aList:
#         if i in bList:
#             l.append(i)
#
#     result = []                 #bu kısım internetten
#     for x in l:
#         if x not in result:
#             result.append(x)
#     return result
#
# x = [4,4,4,4,3,2,1,9,9]
# y = [2,2,2,1,1,4,4,4,4,9,8,7]
#
# print(uniteLists(x, y))

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {"d": 600, "f":256, "g": 123}

# print(d1["b"])
# del d1["c"]
# print(d1)
#
# k = {}
# for key,values in d1.items():
#     k[values] = key
#
# print(k)

# def merge(*dics):
#     d = {}
#     for i in dics:
#         d.update(i)
#
#     print(d)
#
# merge(d1,d2)

dic4 = {}
for d in (d1, d2):
    print(d)
    dic4.update(d)
print(dic4)