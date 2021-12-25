import string
import random

n = 0 #счетчик цифр
N = 0 #большие буквы
nn = 0 #маленькие буквы
S = ''
a = string.ascii_uppercase+string.ascii_lowercase+string.digits
print (a, len (a))
l = random.randint (10,50)
for i in range (0,l,1):
    S = S + a[random.randint(0,61)]
print ('Строка',S,'длинной',l)
    
#поиск цифр
for i in range (0,l,1):
    if (S[i].isdigit()==True):
        n=n+1
print ('Количество цифр:', n)

#поиск маленьких букв
for j in range (0,l,1):
    if (S[j].islower()==True):
        nn = nn + 1
print ('Количество маленьких букв', nn)
