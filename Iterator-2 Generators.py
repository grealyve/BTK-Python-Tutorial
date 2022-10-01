# Bellekte yer işgal etmeyen iterator = Generator

# def cube():
#     result = []
#
#     for i in range(5):
#         result.append(i**3)
#     return result
#
# print(cube())

def cube():
    for i in range(5):
        yield i ** 3        # Bu üretilen değer saklanmıyor, fazla yer kaplamıyor.

generator = cube()

# iterator = iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for i in generator:
    print(i)
##############################################

generator = (i**3 for i in range(5))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# İster fonksiyon oluştur üstteki gibi, ister alttaki gibi comprehensive yap.