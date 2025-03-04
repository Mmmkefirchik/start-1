import wrap, random

wrap.world.create_world(700, 700, 900, 50)


def pas(pers_nomer):
    ugol = wrap.sprite.get_angle(pers_nomer)
    niz = wrap.sprite.get_bottom(pers_nomer)
    vus_a = wrap.sprite.get_height(a) // 2
    shir_ar = wrap.sprite.get_width(a) // 2
    if ugol == 90:
        povorot = wrap.sprite.get_right(pers_nomer)
        wrap.actions.move_to(a, povorot + shir_ar, niz - vus_a)

    elif ugol == -90:
        povorot = wrap.sprite.get_left(pers_nomer)
        wrap.actions.move_to(a, povorot - shir_ar, niz - vus_a)


def beg(pers_nomer, cuda_x, cuda_y):
    wrap.actions.move_to(pers_nomer, cuda_x, cuda_y, 500)


def vedenie(pers_nomer, cuda_x, cuda_y):
    y = wrap.sprite.get_y(pers_nomer)
    x = wrap.sprite.get_x(pers_nomer)
    xa= wrap.sprite.get_x(a)
    popatka = 0
    # ugol = wrap.sprite.get_angle(pers_nomer)
    while popatka != 100:
        if xa<x:
            wrap.sprite.set_reverse_x(pers_nomer,True)
        wrap.sprite.move(pers_nomer, (cuda_x - x) / 100, (cuda_y - y) / 100)
        wrap.sprite.move(a, (cuda_x - x) / 100, (cuda_y - y) / 100)
        popatka = popatka + 1

    y = wrap.sprite.get_y(pers_nomer)
    x = wrap.sprite.get_x(pers_nomer)
    print(x, y)




m1 = wrap.sprite.add('mario-1-big', 300, 200, 'stand')
wrap.sprite.set_reverse_x(m1, True)
m2 = wrap.sprite.add('mario-2-big', 100, 200, 'stand')
c = wrap.sprite.add('mario-enemies', 200, 400, 'crab')
a = wrap.sprite.add('mario-enemies', 200, 300, 'armadillo_egg')
# rezultat=random.choice([m1,m2,c])

pas(m1)
beg(c, 125, 499)
pas(m2)
vedenie(m2,123,677)
pas(m1)
vedenie(m1,499,111)
pas(m2)
vedenie(m2, 350, 50)
pas(c)
vedenie(c, 400, 133)

