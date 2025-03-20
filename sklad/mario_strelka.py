import wrap

wrap.world.create_world(2000,500)

m=wrap.sprite.add('mario-1-big',250,450,'stand')

@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def dvig_niz(keys):
    if wrap.K_LEFT in keys:

        wrap.sprite.set_reverse_x(m,True)

        wrap.sprite.move(m,-5,0)

    if wrap.K_RIGHT in keys:
        wrap.sprite.set_reverse_x(m,False)

        wrap.sprite.move(m,5,0)

@wrap.on_key_down(wrap.K_SPACE)
def polet_podgotovka():
    wrap.sprite.set_costume(m,'swim6')

@wrap.always(20)
def polet(pos_x,pos_y):
    c = wrap.sprite.get_costume(m)
    if c!= 'swim6':
        return
    ugol=wrap.sprite.calc_angle_by_point(m,pos_x,pos_y)

    if ugol!=None:
    # wrap.sprite.set_angle_to_point(m,pos_x,pos_y)
        wrap.sprite.set_angle(m,ugol+90)

    wrap.sprite.move_at_angle_point(m,pos_x,pos_y,5 )

@wrap.on_key_down(wrap.K_DOWN)
def prizemlenie():
    wrap.sprite.set_costume(m,'stand')
    wrap.sprite.set_angle_modif(m,0)
    wrap.sprite.move_to(m,wrap.sprite.get_x(m),450)
















