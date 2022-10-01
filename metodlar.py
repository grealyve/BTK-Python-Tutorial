#method

list = [1,2,3]
list.append(4)      #bu bir method
print(type(list))   #classlar içinde methodlar bulunduran yapı

# fonksiyon

def sayHello(name = "user"):
    print("Hello "+ name)

sayHello()

def total(num1, num2):
    return num1 + num2

result = total(10, 20)
print(result)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

ageAli = yasHesapla(2000)
print(ageAli)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''

    DOCSTRING: Dogum yiliniza göre emekliliginize kaç yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emeklisin")

EmekliligeKacYilKaldi(2001, "Ali")
print(help(EmekliligeKacYilKaldi))

