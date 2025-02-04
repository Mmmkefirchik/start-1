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
time_final = 62#time2 - time1
w = time_final%60
g=str(time_final%60)


    # g=str(int(time_final))+' секунд'
if int(time_final-g)%60==0:
    # w=str(int(time_final))+ 'минут'
    w=str(int(time_final))
if time_final<60 or time_final%60!=0:
    g=str(int(time_final%60))+ ' секунд'
print('Время работы - '+str(w)+" минут"+' и '+str(g))