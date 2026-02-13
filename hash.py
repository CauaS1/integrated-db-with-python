import hashlib
import os

# Salt to avoid rainbow tables
salt = os.urandom(16)


# Initial hash for yor password
hs = hashlib.md5()
hs.update(salt + b"hello")
nwKey = hs.hexdigest()

# Hash of your input
password = input("Your password: ")
ps = hashlib.md5()
ps.update(salt + password.encode())
psHash = ps.hexdigest()

if nwKey == psHash:
    print('Your password is correct')
    print(psHash)
else:
    print('Your password is wrong')
