# error handling => hata yönetimi

#print(a) => NameError
# int("1a2") => ValueError
# print(10/0) => ZeroDivisionError
# print("denem"e) => SyntaxError

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:         # Hata türünü yazmak zorunda değilsin log tutmak için lazım olur sadece.
#     print("y için 0 girilemez")
# except ValueError:
#     print("x ve y için sayısal değer gir!")
# except (ZeroDivisionError, ValueError) as e:
#     print("Yanlış bilgi girdiniz!")
#     print(e)
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as e:
        print("Yanlış bilgi girdiniz", e)
    else:
        break
    finally:
        print("try except sonlandı")