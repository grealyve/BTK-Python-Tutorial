#Referans türünden bir parametre tanımladığımız için fonksiyonun içinde ve dışındaki adresler aynı oluyor
# ad = "Ali" gibi yapsaydık sadece fonksiyonun içine bu değerler kopyalanacaktı ve dışardaki değerler değişmeyecekti
# numara = 2143253241

SadikHesap = {
    "isim": "Sadık Turan",
    "numara": "13245678",
    "bakiye": 3000,
    "ekHesap": 2000
}
AliHesap = {
    "isim": "Ali Turan",
    "numara": "12345678",
    "bakiye": 2000,
    "ekHesap": 1000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['isim']}")
    if miktar <= hesap["bakiye"]:
        hesap["bakiye"] -= miktar
        print("Paranı alabilirsin.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if (toplam >= miktar):
            choice = int(input("1-Ek hesabı kullan, 2- Ek hesabı kullanma: "))
            if choice == 1:
                ekhesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapKullanilacakMiktar
                print("Paranı alabilirsin!")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['numara']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır")

        else:
            print("Yetersiz Bakiye!")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['numara']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır, Ek hesap limitinizde ise {hesap['ekHesap']}")

paraCek(SadikHesap, 3000)

print("***********************")
paraCek(SadikHesap, 2000)
