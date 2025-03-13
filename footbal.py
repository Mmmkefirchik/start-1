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
    xa = wrap.sprite.get_x(a)
    popatka = 0
    # ugol = wrap.sprite.get_angle(pers_nomer)
    if cuda_x > x:
        prav_granic = wrap.sprite.get_right(pers_nomer)
        wrap.actions.move_left_to(a, prav_granic, 200)
        wrap.sprite.set_reverse_x(pers_nomer, False)
    if cuda_x < x:
        lev_granic = wrap.sprite.get_left(pers_nomer)
        wrap.actions.move_right_to(a, lev_granic, 200)
        wrap.sprite.set_reverse_x(pers_nomer, True)

    while popatka != 100:
        if xa < x:
            pass
            # wrap.sprite.set_reverse_x(pers_nomer,True)
        wrap.sprite.move(pers_nomer, (cuda_x - x) / 100, (cuda_y - y) / 100)
        wrap.sprite.move(a, (cuda_x - x) / 100, (cuda_y - y) / 100)
        popatka = popatka + 1

    y = wrap.sprite.get_y(pers_nomer)
    x = wrap.sprite.get_x(pers_nomer)
    print(x, y)


def otbor(pers_nomer):
    xa = wrap.sprite.get_x(a)
    x_p_n=wrap.sprite.get_x(pers_nomer)
    if xa>=x_p_n:
        shir_p = wrap.sprite.get_width(pers_nomer) // 2
        shir_a = wrap.sprite.get_width(a) // 2
        niz_a = wrap.sprite.get_bottom(a)
        niz_p = wrap.sprite.get_height(pers_nomer) // 2
        wrap.actions.move_to(pers_nomer, xa - shir_a - shir_p, niz_a - niz_p)
    if xa<=x_p_n:
        shir_p = wrap.sprite.get_width(pers_nomer) // 2
        shir_a = wrap.sprite.get_width(a) // 2
        niz_a = wrap.sprite.get_bottom(a)
        niz_p = wrap.sprite.get_height(pers_nomer) // 2
        wrap.actions.move_to(pers_nomer, xa + shir_a + shir_p, niz_a - niz_p)


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
otbor(c)
pas(m1)
vedenie(m1,499,111)
pas(m2)
vedenie(m2, 350, 50)
pas(c)
vedenie(c,77,89)
otbor(m2)
vedenie(m2, 400, 133)
