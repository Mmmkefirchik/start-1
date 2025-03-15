import wrap

wrap.world.create_world(2000,500)

m=wrap.sprite.add('mario-1-small',250,475,'stand')

@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def dvig_niz(keys):
    if wrap.K_LEFT in keys:

        wrap.sprite.set_reverse_x(m,True)

        wrap.sprite.move(m,-5,0)

    if wrap.K_RIGHT in keys:
        wrap.sprite.set_reverse_x(m,False)

        wrap.sprite.move(m,5,0)

