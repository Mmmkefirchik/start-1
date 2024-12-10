vsego=int(input('Сколько вишен вы получили?'))
vsego1 = str(vsego)
vsego2=vsego%10

if vsego==0:
    print('Вы получили 0 вишен')

elif vsego==1:
    print('Вы получили 1 вишню')

elif vsego>=2 and vsego<=4:
    print('Вы получили '+vsego1+' вишни')

elif vsego>=5 and vsego<=20:

    print('вы получили '+vsego1+' вишен')

elif vsego2==1:
    print('Вы получили '+vsego1+' вишню')

elif vsego2>=2 and vsego2<=4:
    print('Вы получили '+vsego1+' вишни')

# elif (vsego2>=5 and vsego2<=9) or vsego2==0:
#     print('Вы получили '+vsego1+' вишен')

else:
    print('Вы получили '+vsego1+' вишен')

































































