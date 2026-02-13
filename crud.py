import mysql.connector

connec = mysql.connector.connect(user='root', password='1234567', database='lab')
cursor = connec.cursor() #Tool that talks to the database

option = int(input('Choose what you will do: '))


def table_exits ():
    cursor.execute(
        "SELECT EXISTS (" 
        "SELECT 1 FROM INFORMATION_SCHEMA.TABLES " 
        "WHERE TABLE_SCHEMA = 'lab' and TABLE_NAME = 'users'" 
        ") AS table_exists"
    )

    res = cursor.fetchall()
    res = res[0][0] # 0 = dont exist | 1 = exits

    if res == 0:
        cursor.execute(
            "CREATE TABLE users (" 
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "name VARCHAR(20),"
                "email VARCHAR(50),"
                "salt TEXT,"
                "password TEXT"
                
            ")"
        )
        connec.commit()
    
table_exits()


""" def create_user ():
    name = input("your username: ")
    email = input("your email: ")
    password = input("your password: ")

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    connec.commit()

def read_user():

    name = input("Your name, please: ")
    lis = []
    lis.append(name)
    cursor.execute(
        "SELECT * FROM users WHERE name = %s",
        lis
    )
    result = cursor.fetchall()

    print(result)

match option:
    case 1:
        create_user()
    case 2:
        read_user()
"""

