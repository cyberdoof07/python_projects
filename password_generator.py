import string
import random

a = string.ascii_uppercase+string.ascii_lowercase+string.digits
print(a)
S = ''
r = (int(input('Введите количество символов')))
for i in range (0,r,1):
    S = S + a[random.randint(0,len(a))]
print(S)
