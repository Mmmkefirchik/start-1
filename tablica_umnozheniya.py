import random,time


print('Вас приветствует тестировщик таблиц!')
papatka=1
papatka2=1

na_chto=random.randint(2,9)
cacaya=random.randint(2,9)
time1=time.time()#10
while papatka<2:

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

time2 = time.time()  # 11
time_final = time2-time1#time2 - time1
min=time_final//60
sec=time_final%60

print('Время работы - '+str(int(min))+' мунуту(ы) и ' +str(int(sec))+' секунд(ы)')
#Берем число (62) и находим целую(ые) часть(и) 60 (62//60=1).time_final, получаем кол-во минут.
#Далее нужно вычесть из 62 наш результат (62%60==2).time_final, получаем кол-во сек.