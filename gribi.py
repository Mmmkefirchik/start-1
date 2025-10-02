import wrap, random

wrap.world.create_world(500, 500)

gribi = []
colvo_grib = len(gribi)


@wrap.always(1000)
def poyavlenie():

    a={
        'nomer':wrap.sprite.add('mario-items', random.randint(0, 500), random.randint(0, 500), 'star'),
        "speed_x":random.choice([random.randint(-10,-1),random.randint(1,10)]),
        "speed_y":random.choice([random.randint(-10,-1),random.randint(1,10)])
    }
    gribi.append(a)
    print(gribi)

@wrap.always()
def dvizh ():
    for zvezda in gribi:


        wrap.sprite.move(zvezda['nomer'],zvezda['speed_x'],zvezda['speed_y'])

    # for tolchok_prav_gran in gribi:
        if wrap.sprite.get_right(zvezda['nomer'])>=500:
            zvezda['speed_x']=-abs(zvezda['speed_x'])

        if wrap.sprite.get_left(zvezda['nomer'])<=0:
            zvezda['speed_x']=abs(zvezda['speed_x'])

        if wrap.sprite.get_top(zvezda['nomer'])<=0:
            zvezda['speed_y']=abs(zvezda['speed_y'])

        if wrap.sprite.get_bottom(zvezda['nomer'])>=500:
            zvezda['speed_y']=-abs(zvezda['speed_y'])

