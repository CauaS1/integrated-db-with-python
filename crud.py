import mysql.connector
import hashlib
import os

# Salt to protect the db from rainbow tables
saltValue = os.urandom(16)

# Password hash
def passwordHash(passw, salt):    
    print(salt)

    if isinstance(passw, str):
        password = passw.encode()
    if isinstance(salt, str):
        salt = bytes.fromhex(salt)
        
    hs = hashlib.md5()
    hs.update(salt + password)
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

    storedPassword = passwordHash(password, saltValue)

    cursor.execute(
        "INSERT INTO users (name, email, salt, password) VALUES (%s, %s, %s, %s)",
        (name, email, saltValue.hex(), storedPassword)
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
    saltRe = cursor.fetchall()
    print(saltRe)

def update_username():
    nameExisted = input("Type your current name you want to change? ")
    newName = input("Type your new name: ")
    email = input("Confirm your email: ")

    # Update function
    cursor.execute(
        "UPDATE users SET name = (%s) WHERE name = (%s) AND email = (%s)",
        (newName, nameExisted, email)
    )

    connec.commit()

def update_email():
    oldEmail = input("Type your current email you want to change: ")
    newmEmail = input("Type your new email: ")
    password = input("Confirm your current email's password: ")

    # Getting salt from the database
    lis = []
    lis.append(oldEmail)

    cursor.execute(
        "SELECT salt FROM users WHERE email = (%s)",
        (lis)   
    )

    saltResult = cursor.fetchall()
    saltResult = saltResult[0][0]

    storedHashPassword = passwordHash(password, saltResult)
    print(saltResult)
    print(storedHashPassword)

    cursor.execute(
        "UPDATE users SET email = (%s) WHERE email = (%s) AND password = (%s)",
        (newmEmail, oldEmail, storedHashPassword)
    )

    connec.commit()

def change_password():
    email = input("Type your email: ")
    passwd = input("Type your CURRENT password: ")
    newPasswd = input("Type your NEW password: ")

    lis = []
    lis.append(email) # email inside a list

    cursor.execute(
        "SELECT password, salt FROM users WHERE email = (%s)",
        (lis)
    )

    lis = cursor.fetchall()
    print(lis)

    storedOldHashPassword = passwordHash(passwd, lis[0][1])
    
    storedNewHashPassword = passwordHash(newPasswd, lis[0][1])

    cursor.execute(
        "UPDATE users SET password = (%s) WHERE email = (%s) AND password = (%s)",
        (storedNewHashPassword, email, storedOldHashPassword)
    )

    connec.commit()


match option:
    case 1:
        create_user()
    case 2:
        read_user()
    case 3: 
        update_username()
    case 4:
        update_email()
    case 5:
        change_password()
        