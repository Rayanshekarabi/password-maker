import string 
import random

while True:
    lenght = int(input("please enter your number of password:"))
    chars = string.ascii_letters + string.digits + '!@#$%^&*-+'

    text = []
    for i in range(lenght):
        text.append(random.choice(chars))

    password = "".join(text)

    print(f"this is your password :{password}")    