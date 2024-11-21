# if 3>4:
#     print(1,2,3)
#
# print('конец')
#
# if False:
#     print(232323)
#
kod=3790

otvet=input('Введите пароль')
otvet=int(otvet)

if kod==otvet:
    print('Добро пожаловать!')

if otvet!=kod:
    print('Пароль не верный:(')

print('Конец')