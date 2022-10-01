import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products Where name LIKE '%Samsung%'")   # id=1 | and | or | kullanabilirsin
# name='Samsung S8' and price=3000
# name LIKE 'Samsung%' Samsungla başlayan herhangi bir şeyle biten. Sonundakini silersen de tam tersi olur.

    result = cursor.fetchall()    # bütün kayıtları getirir. liste içinde tuple'lar halinde gelir. hep liste içinde olur
    # result = cursor.fetchone()     # bulduğu ilk kaydı tuple olarak verir. for döngüsüyle yazdıramazsın

    for product in result:
        print(f"id: {product[0]},name: {product[1]} , price: {product[2]}")

def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()
    print(f"id: {result[0]},name: {result[1]} , price: {result[2]}")

getProductById(2)