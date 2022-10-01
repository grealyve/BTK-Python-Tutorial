import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"  # Yer tutucu olarak %s
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()     # Sorgu databaseye gönderiliyor
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"  # Yer tutucu olarak %s
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()     # Sorgu databaseye gönderiliyor
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

list = []
while True:
    name = input("ürün adı: ")
    price = input("ürün fiyatı: ")
    imageUrl = input("ürün resim adı: ")
    description = input("ürün açıklaması: ")

    list.append((name, price, imageUrl, description))

    result = input("Devam etmek istiyor musunuz? (E/H)")

    if result == "h":
        print("Kayıtlarınız veritabanına aktarılıyor...")
        print(list)
        insertProducts(list)
        break

# insertProduct(name, price, imageUrl, description)