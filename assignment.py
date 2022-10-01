x, y ,z = 5, 16, 20
print(x, y, z)

x, y = y, x
print(x, y, z)

x += 5         # x = x + 5
x *= 5         # x = x * 5
x /= 5         # x = x / 5
x %= 5         # x = x % 5
y //= 5         # y = y // 5
y **=  z         # y = y ** z

values = 1, 2, 3
values1 = 1, 2, 3, 4, 5
print(type(values))

x, y, z = values
k, l, *m = values1

print(k, l, m)


