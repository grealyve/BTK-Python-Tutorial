#global scope
x = "global x"

def function():
    #local scope
    x = "local x"   #yorum satırı olsaydı fonksiyon da global scope'u kullanacaktı
    print(x)

function()
print(x)

#######################

name = "Çınar"

def changeName(new_name):
    name = new_name
    print(name)

changeName("Ada")
print(name)

#######################

name = "gloal string"

def greeting():
    name = "Çınar"

    def hello():
        #name = "Ada"
        print("hello " + name) #burda kullandığın name bir üstteki scope'dakini alır
                                #bu fonksiyon için global scope, bir üst scope'dur
    hello()

greeting()

#######################

x=50
def test():
    global x        #bunu yazarsan globaldeki değeri de değiştirir.
    print(f"x : {x}")

    x= 100
    print(f"changed x to {x}")

test()
print(x)