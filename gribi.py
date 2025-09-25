import wrap, random

wrap.world.create_world(500, 500)

gribi = [wrap.sprite.add('mario-items', 5, 150, 'star'), wrap.sprite.add('mario-items', 15, 50, 'star'),
         wrap.sprite.add('mario-items', 10, 100, 'star')]


@wrap.always(5000)
def poyavlenie():
    gribi.append(wrap.sprite.add('mario-items', random.randint(0, 500), random.randint(0, 500), 'star'))
