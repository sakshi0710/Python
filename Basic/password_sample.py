import random

passlen=8
password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567891@#$%^&*"

user_password= random.sample(password,passlen)
#users= ''.join(user_password)
users = ''.join(str(x) for x in user_password)
print("Your password is:", users)