## Integrated Database with Python

A small backend project built with Python and mysql.connector that implements a complete CRUD system for user management.
The goal of this project is to practice database integration, password handling, and structured backend logic.

## Database Initialization

Checks if the users table exists.
If it does not exist, the table is automatically created with the following fields:
* name
* email
* salt
* password

## Functionalities:
  * **A system that checks if the table `users` exists, if doens't, it will create one with the following values**
    * name, email, salt, password
  * **Adds a new user to the database with hashed and salted password**
      * ⚠️ Note: the password system uses `hashlib` to create a MD5 hash for the password (I know MD5 is not recommended for passwords, since it's a fast encrypted system, and it's easy for brute for attacks)
          * Future upgrades may include Argon2/Bcrypt for password storage.
      * the password uses a **salt** to prevent Rainbow Table attacks
  * **Checking system to show your name and email inside the database**
      * Future upgrades will improve security measures to forbid you of getting another user's info with the same username as yours
  * **Change your email**
      * you need to check and compare the hash password first to make any changes.
  * **Change your password after confirming your email and old password**
  * **Delete account system**

## Future Upgrades
 * **Optmize the code:**
      * `passwordHash()` can be improved, specially to retrieve the password
 * **Implements issues manegment:**
      * Add messages to explaining possible errors
      * Create a system to avoid bugs:
           * If you check and inexistent user account, it will result in error


