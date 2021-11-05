from random import choice

pwd_length=8
pwd_valid_chars="abcdefghijklmnopqursuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"


new_passwd=[]
for each_char in range(pwd_length):
    new_passwd.append(choice(pwd_valid_chars))

random_passwd= ("".join(new_passwd))
print (random_passwd)


