import wrap, random

pushka_ur1 = None
wrap.add_sprite_dir('sklad')
wrap.world.create_world(500, 500)

gribi = []
puli = []
kapital = wrap.sprite.add_text(str(0), 50, 50, text_color=(255, 255, 0), font_size=40)

colvo_grib = len(gribi)
kolvo_monet = 0
moneta_na_krane = wrap.sprite.add('proekt_gribi', 85, 50, 'moneta')
wrap.sprite.set_size_percent(moneta_na_krane, 10, 10)

PUSHKA_NE_PRODAYOTSA = 0
PUSHKA_V_PRODAZHE = 1
PUSHKA_KUPLENA = 2
pushka_zapusk = PUSHKA_NE_PRODAYOTSA
ugol = 5

check_na_zaskok = False
x = 0
y = 0
distanciya = 5
def delete_zvezd(x, y):
    a = poisk_zvezd_po_koordinatam(x, y)

    if a == None:
        return

    wrap.sprite.remove(a['nomer'])

    gribi.remove(a)
    return True

def plus_money(dohod=1):
    global kolvo_monet
    kolvo_monet = kolvo_monet + dohod
    wrap.sprite_text.set_text(kapital, str(kolvo_monet))



def poisk_zvezd_po_koordinatam(x, y):
    for zvezda in gribi:
        if wrap.sprite.is_collide_point(zvezda['nomer'], x, y):
            return zvezda


def zbivanie_zvezd():
    if pushka_zapusk != PUSHKA_KUPLENA:
        return

    for pula in puli.copy():
        x_pola = wrap.sprite.get_x(pula['nomer'])
        y_pola = wrap.sprite.get_y(pula['nomer'])

        if delete_zvezd(x_pola, y_pola) == None:
            continue

        wrap.sprite.remove(pula['nomer'])
        puli.remove(pula)
        plus_money()


@wrap.always(1000)
def poyavlenie():
    a = {
        'nomer': wrap.sprite.add('mario-items', random.randint(0, 500), random.randint(0, 500), 'star'),
        "speed_x": random.choice([random.randint(-10, -1), random.randint(1, 10)]),
        "speed_y": random.choice([random.randint(-10, -1), random.randint(1, 10)])
    }
    gribi.append(a)
    # print(gribi)


@wrap.always()
def dvizh():
    for zvezda in gribi:

        wrap.sprite.move(zvezda['nomer'], zvezda['speed_x'], zvezda['speed_y'])

        if wrap.sprite.get_right(zvezda['nomer']) >= 500:
            zvezda['speed_x'] = -abs(zvezda['speed_x'])

        if wrap.sprite.get_left(zvezda['nomer']) <= 0:
            zvezda['speed_x'] = abs(zvezda['speed_x'])

        if wrap.sprite.get_top(zvezda['nomer']) <= 0:
            zvezda['speed_y'] = abs(zvezda['speed_y'])

        if wrap.sprite.get_bottom(zvezda['nomer']) >= 500:
            zvezda['speed_y'] = -abs(zvezda['speed_y'])
    zbivanie_zvezd()





@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def zbor_zvezd(pos_x, pos_y):
    global kolvo_monet, pushka_knopka, pushka_zapusk

    if delete_zvezd(pos_x, pos_y) == None:
        return

    plus_money()
    if kolvo_monet >= 10 and pushka_zapusk == PUSHKA_NE_PRODAYOTSA:
        pushka_knopka = wrap.sprite.add('proekt_gribi', 450, 50, 'pushka')

        pushka_zapusk = PUSHKA_V_PRODAZHE


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def prodasza_pushki(pos_x, pos_y):
    global pushka_zapusk, pushka_ur1,kolvo_monet

    if pushka_zapusk == PUSHKA_KUPLENA or pushka_zapusk == PUSHKA_NE_PRODAYOTSA:
        return
    if wrap.sprite.is_collide_point(pushka_knopka, pos_x, pos_y):
        wrap.sprite.remove(pushka_knopka)

        pushka_ur1 = wrap.sprite.add('proekt_gribi', 250, 500, 'bashna1')
        wrap.sprite.set_size_percent(pushka_ur1, 45, 45)
        wrap.sprite.set_angle(pushka_ur1, 0)
        pushka_zapusk = PUSHKA_KUPLENA

        plus_money(-10)





@wrap.always()
def strelba_is_pushki(pos_x, pos_y):
    global ugol, check_na_zaskok
    if pushka_zapusk != PUSHKA_KUPLENA:
        return

    ugol_pushki = wrap.sprite.get_angle(pushka_ur1)
    if ugol_pushki >= 90:
        check_na_zaskok = True
    if ugol_pushki < -90:
        check_na_zaskok = False

    if check_na_zaskok == False:
        ugol = ugol + 5

    if check_na_zaskok == True:
        ugol = ugol - 5

    wrap.sprite.set_angle(pushka_ur1, ugol)





@wrap.always(1000)
def strelba():
    if pushka_zapusk != PUSHKA_KUPLENA:
        return

    ugol_pushki = wrap.sprite.get_angle(pushka_ur1)
    x_y = wrap.sprite.get_pos(pushka_ur1)

    pula = wrap.sprite.add('pacman', x_y[0], x_y[1], 'dot')
    pula_coordinat = {'nomer': pula,
                      'ugol': ugol_pushki}

    puli.append(pula_coordinat)

    wrap.sprite.move_at_angle(pula, ugol_pushki, 140)





@wrap.always()
def polet_pul():
    global distanciya
    for pula in puli:
        xy = wrap.sprite.get_pos(pula['nomer'])

        if xy[0] >= 500 or xy[0] < 0 or xy[1] < 0:
            puli.remove(pula)

        wrap.sprite.move_at_angle(pula['nomer'], pula['ugol'], distanciya)
        print(len(puli))
    zbivanie_zvezd()


import wrap_py

wrap_py.app.start()
