import random

print('Вас приветствует тестировщик таблиц!')
papatka=1
papatka2=1
na_chto=random.randint(2,9)
cacaya=random.randint(2,9)
while papatka<10:


    my_otvet=input(str(papatka)+') Сколько будет '+str(cacaya)+'*'+str(na_chto)+'? ('+str(papatka2)+')')
    papatka2=papatka2+1
    if my_otvet.isnumeric() == True:
        my_otvet=int(my_otvet)
    else:
        print('Пишите цифры!')
    if cacaya*na_chto==my_otvet:
        print('правильно')
        # papatka=papatka+1
        na_chto = random.randint(2, 9)
        cacaya = random.randint(2, 9)
        # papatka2=1

    else:
        print('неправильно')

    if cacaya*na_chto==my_otvet and my_otvet.isnumeric()==False:
        papatka=papatka+1
        papatka2+papatka2+1
