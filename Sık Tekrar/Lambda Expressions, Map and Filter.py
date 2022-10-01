'''def square(num): return num ** 2

numbers = [1,3,5,9]     #for döngüsü yerine map metodunu kullanıyoruz
result = list(map(square, numbers)) #yazdırınca bellek üzerinde bir adresle döner bunu çalıştırmak için list ya da for döngüsüyle olur
print(result)

for item in map(square, numbers):
    print(item)

print(result)   '''

'''numbers = [1,3,5,9]
#lambda metoduyla isimsiz bir fonksiyon yaratabilirsin
result = list(map(lambda num: num ** 2, numbers))

print(result) 
#bu şekilde lambda'yı isimlendirebilirsin
square = lambda num: num ** 2

numbers = [1,3,5,9]

result = list(map(square, numbers))
result = square(3)
print(result)

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')

(lambda x, y: x + y)(2, 3)

high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)
6
high_ord_func(2, lambda x: x + 3)
7

   '''

#FİLTER

numbers = [1,3,5,9,10,4,6]

def check_even(num): return num%2==0

#result = list(filter(check_even, numbers))
result = list(filter(lambda num: num%2==0 , numbers))

result2 = check_even(numbers[2])

print(result)
print(result2)