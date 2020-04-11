import random
import string

letters= string.ascii_letters
digit= string.digits
special_characters= string.punctuation
password = letters+digit+special_characters
valid = True

while valid:
    passlen = int(input("enter the the password length. Your password length min:8 and max: 16"))
    if passlen >= 8 and passlen <= 16:
        user_password = ''.join(str(x) for x in random.sample(password, passlen))
        print("Your password is:", user_password)
        break
    else:
        print("please give the correct password length")



