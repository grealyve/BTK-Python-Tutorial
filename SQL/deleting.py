import mysql.connector

def deleteProduct(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    # sql = "delete from products where id=4"
    # sql = "delete from products where name like '%s7%'"
    # sql = "delete from products where id=%s"
    sql = "delete from products where id="+id   # böyle yaparsan sql injectiona karşı açık olur
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt")

    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")


deleteProduct(5)