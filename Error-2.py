
# x = 10
#
# if x > 5:
#     raise Exception("x 5 den büyük değer alamaz.")

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise  Exception("parola en az 7 karakter olmalıdır")
#     elif not re.search("[a-z]", psw):
#         raise Exception("parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("parola alpha numeric karakter içermelidir.")
#     elif re.search("\s", psw):
#         raise Exception("parola boşluk içermemeli")
#     else:
#         print("geçerli parola")
# password = "1234567a8Z_"
#
# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola: else")
# finally:
#     print("Validation tamamlandı.")

class Person:
    def __init__(self,name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name = name
            self.year = year

p = Person("Aliiiiiiiiiiiiiiiiiii", 1992)