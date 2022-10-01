import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By name, price")  # Order By price DESC azalana göre sıralar
    # name, price yazarsan grubun içinde de sıralama yapar.

    result = cursor.fetchall()

    for product in result:
        print(f"id: {product[0]},name: {product[1]} , price: {product[2]}")

getProducts()