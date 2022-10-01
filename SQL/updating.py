import mysql.connector

def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()
    print(f"id: {result[0]},name: {result[1]} , price: {result[2]}")

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    if name!='':
    # sql = "Update products Set name='Samsung S10' where id=5"   # where yazmazsan bütün name'leri s10 yapar
        sql = "Update products Set name=%s, price=%s where id=%s"
    values = (name, price, id)

    cursor.execute(sql, values)
    
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt")

    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

updateProduct(1, "Ihone 8", 6000)