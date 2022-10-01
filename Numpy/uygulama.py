import numpy as np

# result = np.array([10,15,30,45,60])
# result = np.arange(5,15)
# result = np.arange(50,100,5)
# result = np.zeros(10)
# result = np.ones(10)
# result = np.linspace(0,100,5)
# result = np.random.randint(10,30,5)
# result = np.random.randn(10)

result = np.random.randint(10,50,15).reshape(3,5)
# print(result.sum(axis=1), result.sum(axis=0))

# print(result.max(), result.min(), result.mean())
# print(result.argmax(), result.argmin())

# numberss = np.arange(10,20)
# result = numberss[:3]
# result = numberss[::-1]

# print(result[0,:])
# print(result[1,2])
# print(result[:,0])
# sqrst = np.power(result, 2)
# print(sqrst)

numberss = np.arange(-50, 50)
result1 = numberss[numberss >= 0]
result2 = result1[result1 % 2 == 0]
print(result2)