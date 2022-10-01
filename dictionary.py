# key - value

sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("istanbul")])

#print(plakalar["kocaeli"]) => 41

plakalar = {"kocaeli" : 41, "istanbul" : 34}

print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"] = 6
plakalar["kocaeli"] = "new value"
print(plakalar)

users = {
    "sadikturan": {
        "age": 36,
        "roles": ["user"],   #bir web sitesi yaptığında bu kim hangi role sahipse ona göre bir şeye erişebilir
        "email": "sadik@gmail.com",
        "phone": "123213214",
        "address": "kocaeli"
    },
    "cinarturan": {
        "roles": ["admin", "user"],
        "age": 2,
    },
}
print(users["sadikturan"])
print(users["sadikturan"]["age"])
print(users["cinarturan"]["roles"][0])
