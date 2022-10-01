import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    # sql = "Select * From Products"
    # sql = "Select * From Categories"
    # sql = "Select * From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where Categories.name='Telefon'"
    sql = "Select p.name,p.price,c.name From Products as p inner join Categories as c on c.id=p.Categoryid where p.name='Samsung s5'"

    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

getProducts()