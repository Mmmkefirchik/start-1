zhelezo=100
instrument=7
gvozd=2
gvozd2=zhelezo//instrument
ostatok_vsego=zhelezo%instrument#100-98
a=ostatok_vsego//gvozd
zatrati_na_gvozd=a*gvozd#2кг
b=ostatok_vsego%gvozd




print('У нас было ',zhelezo,'кг. железа.')
print('На один инструмент у нас уходило',instrument,'кг. железа')
print('А на один гвоздь у нас уходило',gvozd,'кг. железа.')
print("Сколько инструментов мы сможем изготовить из",zhelezo,'кг железа?')
print('И сколько гвоздей мы сделаем из остатков?')
print('сколько кг железа останется не использовынными?')
print()
print("Из",zhelezo,'кг железа, мы сможем сделать',zhelezo//instrument,'инструментов')
print('А из остатков железа мы сделаем',a,'гвоздей')
print()
print('Осталось неиспользованнымикг',b,'кг железа')
# print(import2)