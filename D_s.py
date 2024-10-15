vsego=43
stoimost=6

oplachen_chocolate=vsego//stoimost
podar_chocolate=oplachen_chocolate//2
vsego_cop_chocolate=oplachen_chocolate+podar_chocolate

ostatok_deneg=stoimost*oplachen_chocolate
a=vsego-ostatok_deneg
print('В супермаркете проходит акция: 3 шоколадки по цене 2')
print('одна шоколадка стоит',stoimost,'рубль')
print('У покупателе есть',vsego,'рубля')
print('Он сможет купить',vsego_cop_chocolate,'шоколадок')
print('А останется',a,'рублей')