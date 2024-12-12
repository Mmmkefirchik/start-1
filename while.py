import random

rezoltat=random.randint(1,10000)#1
otvet=-1000

popatka = 0
# if
while rezoltat!=otvet:
    popatka = popatka + 1
    otvet = input(str(popatka)+') пароль?')

    if otvet.isnumeric()==False:
        continue
    otvet=int(otvet)

    if rezoltat>otvet:
        print('Больше')

    if rezoltat<otvet:
        print('Меньше')
else:
   print('вы угадали')