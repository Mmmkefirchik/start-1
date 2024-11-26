print("Можно, пожалуйста, билет  на 'Техасская резня бензопилой' ?")

otvet=input('Сколько вам лет?')
otvet=int(otvet)

if otvet<=11 and otvet>=7:
    print('К сожалению, до 12 лет нельзя смотреть данный фильм')

if otvet<=6 and otvet>=0:
    print('Я тебе не верю! Ты бы не дотянулся да кассы!')
    otvet=input('Так сколько тебе лет на самом деле?')
    otvet=int(otvet)

if otvet>=12 and otvet<=16:
    otvet2=input('А родители с тобой придут?')

    if otvet2=='да':
        print('Когда придут - тогда и поговорим')
    else:
        print('До 16 без родителей нельзя')

if otvet>16 and otvet<100:
    print('Да, конечно')

if otvet>=100:
    print('Я думаю ваша психика не выдержет данного контента')

