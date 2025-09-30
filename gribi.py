import wrap, random

wrap.world.create_world(500, 500)

gribi = []
colvo_grib = len(gribi)


@wrap.always(1000)
def poyavlenie():
    a={
        'nomer':wrap.sprite.add('mario-items', random.randint(0, 500), random.randint(0, 500), 'star'),
        "napravlenie_x":random.randint(-10,10),
        "napravlenie_y":random.randint(-10,10)
    }
    gribi.append(a)
    print(gribi)

@wrap.always()
def dvizh ():
    for dvizh_pravo in gribi:


        wrap.sprite.move(dvizh_pravo['nomer'],dvizh_pravo['napravlenie_x'],dvizh_pravo['napravlenie_y'])



