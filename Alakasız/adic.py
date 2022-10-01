# eng2sp = {}
#
# eng2sp['one'] = 'uno'
# eng2sp['two'] = 'dos'
# eng2sp['three'] = 'tres'

###################### SIRALAMA VEYA TERS ÇEVİRİP SIRALAMA ************
'''
dic = {1:20, 0: 41, 8: 113, 5: 12}
a = sorted(dic.items(), reverse=True)
print(a)'''

###################### Dictionaryleri toplama ***************

# def addDic(dic):
#     diction = {}
#     for key, value in dic.items():
#         diction[key] = value
#     return diction

def addDicc(*dicts):
    result = dict()
    for d in dicts:
        result.update(d)
    return result

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)                      # DEMEKKİ BÖYLE BİR ŞEY VARMIŞ
print(dic4)
print(addDicc(dic1,dic2,dic3))
####################
# d = {}
# n = 5
# for i in range(n):
#     key = i
#     value = i*i
#     d[key] = value
# print(d)
# for x in range(1,n+1):
#     d[x]=x*x
#######################
# d = dict()
# for x in range(1,15):         Böyle de bir şey varmış
#     d[x] = x*x
# print(d)
#########################
# def merge(d1,d2):
#     for key, values in d1.items():
#         d2[key] = values
#     print(sorted(d2.items()))
#
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# merge(dic1,dic2)
# def merge_dictionaries(*dicts):
#   result = dict()
#   print(dicts)
#   for d in dicts:
#     result.update(d)                                              # ÇOK DEĞİŞİK YAKLAŞIM...
#     print(d)
#   return result
# print(merge_dictionaries(dic1,dic2))
#########################
# def addall(dict):
#     print(sum(dict.values()))
#
# my_dict = {'data1':100,'data2':-54,'data3':247}
# addall(my_dict)
#########################
# def multp(dict):
#     a = 1
#     for values in dict.values():
#         a *= values
#     print(a)
#
# my_dict = {'data1':100,'data2':-54,'data3':247}
# multp(my_dict)
#12#########################
# my_dict = {'data1':100,'data2':-54,'data3':247}
# if "data1" in my_dict:
#     del my_dict["data1"]
# print(my_dict)
#
# my_dict = {'data1':100,'data2':-54,'data3':247}
# a = input("Del it: ")
# for key in my_dict.keys():
#     if key == a:
#         del my_dict[a]
#         break
# print(my_dict)
############################
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# d = {}
# for key,value in student_data.items():
#     if value not in d.values():
#         d[key]= value
# print(d)
#################################
# my_dict = {'data1':100,'data2':-54,'data3':247}
# def checking(dict):
#     d = {}
#     if dict == d:
#         print("Boş la bu")
#     else:
#         print("Dolu dolu")
# checking(my_dict)
###################################
def addcom(d1, d2):
    d = {}
    for key1, value1 in d1.items():
            if key1 in d2.keys():
                d[key1] = value1 + d2[key1]
            else:
                if key1 not in d.keys():
                    d[key1] = value1
    for key2, value2 in d2.items():
        if key2 not in d.keys():
            d[key2] = value2
    print(d)
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
addcom(d1, d2)
################## 24 ##################
# d = {}
# samp = 'w3resource'
# for i in samp:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
#########################################
# d1 = {'a': 100, 'b': 200, 'c':300}
# def prpr(dic):
#     for key,value in dic.items():
#         print(f"\t{key}\t|\t {value}\n")
# prpr(d1)
########################################
# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {}
# for x,y in num.items():
#     sorted_dict[x] = sorted(y)     insted         sorted_dict = {x: sorted(y) for x, y in num.items()}
# print(sorted_dict)
########################################
# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# new = {}
# for x,y in student_list.items():
#     x = x.split()
#     x = x[0] + x[1]
#     new[x] = y
# print(new)
##################    32      #######################
students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}

for a in students:
    print(a)
    for b in students[a]:
        print(f"{b} : {students[a][b]}")
##########################################
# a = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# b = [1, 2, 2, 3]
# d = {}
# for i in range(len(a)):
#     d[a[i]] = b[i]
# print(d)
########################################
# d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# result = dict()
# for x,y in d.items():
#     if y > 170:
#         result[x] = y
# print(result)
################      43      ########################
# student_id = ["S001", "S002", "S003", "S004"]
# student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
# student_grade = [85, 98, 89, 92]
#
# def nested_dictionary(l1, l2, l3):
#     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
#     return result
# print(nested_dictionary(student_id, student_name, student_grade))
######################## BU DA HA GÜZEL #########################################
listK = ["Mon", "Tue", "Wed"]
listV = [3, 6, 5]
resulst = dict(zip(listK, listV))

print(resulst)
#################################################################################
# students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
#
# def value_check(students, n):
#     result = all(x == n for x in students.values())
#     return result
#
# print(value_check(students, 12))
#################################################################################
# students = {
#   'Theodore': 10,
#   'Mathew': 11,
#   'Roxanne': 9,
# }
#
# def reverse(dic):
#     return {v : k for k,v in dic.items()}
#
# print(reverse(students))
#                                          2. YOL
# students = {
#   'Theodore': 10,
#   'Mathew': 11,
#   'Roxanne': 9,
# }
# def reverse(dic):
#     l1 = []
#     l2 = []
#     for k,v in dic.items():
#         l1.append(k)
#         l2.append(v)
#     return dict(zip(l2,l1))
#
# print(reverse(students))
#####################################################################################
# a = ['a', 'b', 'c', 'd', 'e', 'f']
# b = [1, 2, 3, 4, 5]
#
# def combine(l1,l2):
#     return dict(zip(l1,l2))
#
# print(combine(a,b))
################################    DİC TO LİST OF TUPLE    #####################################################
# d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# def dictotuple(dic):
#     l = [(k,v) for k,v in dic.items()]
#     return l
#
# print(dictotuple(d))
#####################################################################################
# d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# def listele(dic):
#     return [k for k in dic.keys()]
#
# print(listele(d))
#                 2. YOL
# def test(flat_dict):
#   return list(flat_dict.keys())
# ##########################################################################################
# d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# def minmax(dic):
#     values = [v for v in dic.values()]
#     d = {v: k for k, v in dic.items()}
#     maxi = d[max(values)]
#     mini = d[min(values)]
#     print(f"max {maxi}, min {mini}")
#     # for k,v in dic.items():
#     #     if v == maxi:
#     #         print(f"{k} has the max value.")
#     #     if v == mini:
#     #         print(f"{k} has the min value.")
#
# minmax(d)
d = dict([(3,"three"),(1,"one")])
print(d)

b = [1, 2, 3, 4, 5]
print(list(reversed(b)))

def dellet(letter, string):
    l = []
    for i in string:
        if i == letter:
            del i
        else:
            l.append(i)
    print("".join(l))

dellet("i", "alinin kilitli")