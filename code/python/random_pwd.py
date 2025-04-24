import random
import string
### Author WebSite
### http://18k.icu
### https://blog.csdn.net/OneCrab
### https://github.com/0x7556
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("生成的随机密码是：", generate_password())