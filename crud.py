import mysql.connector

connec = mysql.connector.connect(user='root', password='1234567', database='lab')
cursor = connec.cursor() #Tool that talks to the database

option = int(input('Choose what you will do: '))

def create_user ():
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


