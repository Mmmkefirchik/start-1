import wrap, random
from wrap_mENdRU.sprite import remove

wrap.add_sprite_dir('sklad')
wrap.world.create_world(500, 500)

gribi = []

colvo_grib = len(gribi)


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


kolvo_monet = 0
kapital = wrap.sprite.add_text(str(0), 50, 50, text_color=(255, 255, 0), font_size=40)
moneta_na_krane = wrap.sprite.add('proekt_gribi', 85, 50, 'moneta')
wrap.sprite.set_size_percent(moneta_na_krane, 10, 10)
pushka_zapusk = 0


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def zbor_zvezd(pos_x, pos_y):
    global kolvo_monet, pushka, pushka_zapusk
    zvezda = poisk_zvezd_po_koordinatam(pos_x, pos_y)
    if zvezda == None:
        return

    wrap.sprite.remove(zvezda['nomer'])
    gribi.remove(zvezda)
    kolvo_monet = kolvo_monet + 1
    wrap.sprite_text.set_text(kapital, str(kolvo_monet))

    if kolvo_monet >= 1 and pushka_zapusk == 0:
        pushka = wrap.sprite.add('proekt_gribi', 450, 50, 'pushka')
        pushka_zapusk = 1


def poisk_zvezd_po_koordinatam(x, y):
    for zvezda in gribi:
        if wrap.sprite.is_collide_point(zvezda['nomer'], x, y):
            return zvezda


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def d(pos_x, pos_y):
    global pushka_zapusk

    if pushka_zapusk == 3 or pushka_zapusk==0:
        return

    # if pushka_zapusk!=3:
    if wrap.sprite.is_collide_point(pushka, pos_x, pos_y):
        wrap.sprite.remove(pushka)
        pushka_zapusk = 3
