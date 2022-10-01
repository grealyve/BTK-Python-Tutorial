import numpy as np

# result = np.array([1,3,5,7,9])    # listeyi dizi yapar
# result = np.arrange(1,10)         # dizi oluşturur
# result = np.arange(10, 100,3)     # 3'er 3'er artan bir dizi oluşturur
# result = np.zeros(10)               # 0 lardan oluşan dizi oluşturur
# result = np.ones(10)
# result = np.linespace(0,100,5)      # 5 parçaya bölünmüş bir dizi oluşturur
# result = np.random.randint(0,10)   # sadece üst değeri vererek de yapabilirsin.
# result = np.random.randint(1,10,3)   # random 3 sayılı bir dizi oluşturur
# result = np.random.rand(5)          # 0-1 arası sayılar     randn'lisi negatifleri de alır

# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)       # 5 dikey, 10 yatayda olacak matris oluşturur  5 satır 10 sütun
# print(np_multi.sum(axis=1))         # her satırın toplamını verir

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
# result = rnd_numbers.max()
# result = rnd_numbers.mean()     # ortalamasını verir
# result = rnd_numbers.argmax()   # max olanın indexini verir
result = rnd_numbers.argmin()

print(result)