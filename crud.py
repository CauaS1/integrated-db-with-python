import mysql.connector
import hashlib
import os

# Salt to protect the db from rainbow tables
salt = os.urandom(16)

# Password hash
def passwordHash(passw):    
    encodedPassword = passw.encode()
    hs = hashlib.md5()
    hs.update(salt + encodedPassword)
    encryptePassword = hs.hexdigest()

    return encryptePassword

connec = mysql.connector.connect(user='root', password='1234567', database='lab')
cursor = connec.cursor() #Tool that talks to the database

# Checks if the table exists, if not, it will create one
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

# Input that will give you options of what to do
option = int(input("""
    [1] - Create a new user
    [2] - Read your user info
    [3] - Update your username
    [4] - Update your email
                   
    What you're going to do? Digit the number: 
"""))

def create_user ():
    name = input("your username: ")
    email = input("your email: ")
    password = input("your password: ")

    storedPassword = passwordHash(password)

    cursor.execute(
        "INSERT INTO users (name, email, salt, password) VALUES (%s, %s, %s, %s)",
        (name, email, salt.hex(), storedPassword)
    )
    connec.commit()

def read_user():
    name = input("Your name, please: ")
    lis = []
    lis.append(name)
    cursor.execute(
        "SELECT name, email FROM users WHERE name = %s",
        lis
    )
    result = cursor.fetchall()

    print(result)

def update_username():
    nameExisted = input("Type the name you want to change? ")
    newName = input("Type your new name: ")
    email = input("Confirm your email: ")

    # Update function
    cursor.execute(
        "UPDATE users SET name = (%s) WHERE name = (%s) AND email = (%s)",
        (newName, nameExisted, email)
    )

    connec.commit()

match option:
    case 1:
        create_user()
    case 2:
        read_user()
    case 3: 
        update_username()


