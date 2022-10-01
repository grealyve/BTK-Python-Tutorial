import mysql.connector

def getProductById():
    connection = mysql.connector.connect(host="localhost", user = "root", password = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    # sql = "Select COUNT(*) From Products"
    # sql = "Select AVG(Price) From Products"
    # sql = "Select SUM(Price) From Products"
    # sql = "Select MIN(Price) From Products"
    sql = "Select Name,Price From Products Where Price = (Select MAX(Price) From Products)"


    cursor.execute(sql)

    result = cursor.fetchone()
    print(f"id: {result[0]}, price: {result[1]}")

getProductById()