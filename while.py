import random
vsego=10000
rezoltat=random.randint(1, vsego)#1
otvet=-1000

popatka = 1

while rezoltat!=otvet:
    otvet = input(str(popatka)+') пароль?')
    # a='СДАЮСЬ'
    if otvet.upper()=='СДАЮСЬ':
        print('Я загадала число - ' + str(rezoltat))
        break

    if otvet.isnumeric()==False:
        print('Пишите цифры')
        continue
    # popatka = popatka + 1
    otvet=int(otvet)

    if otvet>vsego:
        print('Макс. числ.- ' + str(vsego))
        continue
    # else:

    # if otvet<=rezoltat:
    if rezoltat>otvet:
        print('Больше')

    if rezoltat<otvet:
        print('Меньше')
    popatka = popatka + 1

else:
   print('вы угадали за '+str(popatka-1)+' попитка')
