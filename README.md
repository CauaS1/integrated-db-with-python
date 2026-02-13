## Integrated Database with Python

It's a small project where I'm using `mysql.conector` on Python to create a CRUD system.

## Functionalities:
  * **A system that checks if the table `users` exists, if doens't, it will create one with the following values**
    * name, email, salt, password
  * **A system that add an user to the table**
      * the password system uses `hashlib` to create a MD5 hash for the password (I know MD5 is not recommended for passwords, since it's a fast encrypted system, and it's easy for brute for attacks)
          * Future upgrades may include Argon2/Bcrypt for password storage.
      * the password uses a **salt** to prevent Rainbow Table attacks
  * **A system that allow sthe user to checks their name and email inside the database**
      * Future upgrades will improve security measures to forbid you of getting another user's info with the same username as yours
  * **A system that allows you to change your email**
