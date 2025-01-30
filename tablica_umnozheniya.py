import random,time


print('Вас приветствует тестировщик таблиц!')
papatka=1
papatka2=1

na_chto=random.randint(2,9)
cacaya=random.randint(2,9)
time1=time.time()#10
while papatka<6:

    time2=time.time()#11
    time_final=time2-time1
    my_otvet=input(str(papatka)+') Сколько будет '+str(cacaya)+'*'+str(na_chto)+'? ('+str(papatka2)+')')
    if my_otvet.isnumeric()==False:
        print('Пишите цифры!')
        continue

    if cacaya*na_chto==int(my_otvet):
        print('правильно')
        papatka=papatka+1
        na_chto = random.randint(2, 9)
        cacaya = random.randint(2, 9)
        papatka2=1
    elif cacaya*na_chto!=int(my_otvet):
        print('неправильно')
        papatka2=papatka2+1


if
# time_final=int(time_final)
# print('Время работы - '+str(time_final))
#