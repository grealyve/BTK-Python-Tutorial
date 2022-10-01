def filterList(aList):
    list1 = []
    for i in aList:
        if i % 6 == 0:
            list1.append(i)
    return list1
deneme = [6,12,321,21,65,60]
print(filterList(deneme))