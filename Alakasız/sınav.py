import random
a = random.randrange(1,10)
b = random.randrange(20,70)
c = int(random.random()) * 5
if a - b < 0 and a + b <= 80:
    a = a ** c
    if a + b < 20:
        a = a ** 2
    else:
        b = b * c + 1
else:
    b = b ** c
    if a + b >= 20:
        b = b ** 2
    else:
        a = a * c + 1

print(a,b,c)