import random

rezoltat=random.randint(1,10)#1
otvet=-1000
while rezoltat!=otvet:
    otvet=input('пароль?')
    otvet=int(otvet)
else:
   print('вы угадали')