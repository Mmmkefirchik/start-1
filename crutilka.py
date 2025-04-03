import  wrap,random
wrap.world.create_world(500,500)

p=wrap.sprite.add('pacman',250,200,'enemy_blue_down2')
m=wrap.sprite.add('mario-1-big',250,300,'stand')
t=wrap.sprite.add('battle_city_tanks',250,100,'tank_enemy_size1_green1')

@wrap.on_key_down(wrap.K_UP,wrap.K_DOWN)
def smena(pos_x,pos_y,key):
    pk=wrap.sprite.is_collide_point(p,pos_x,pos_y)
    mk=wrap.sprite.is_collide_point(m,pos_x,pos_y)
    tk=wrap.sprite.is_collide_point(t,pos_x,pos_y)

    if pk==True:
        zhertva=p
    elif mk==True:
        zhertva = m
    elif tk==True:
        zhertva = t
    else:
        zhertva=None

    if zhertva!=None:
        if key==wrap.K_UP:
            wrap.sprite.set_costume_next(zhertva)
        if key==wrap.K_DOWN:
            wrap.sprite.set_costume_prev(zhertva)
    #
    # if mk == True and key == wrap.K_UP:
    #     wrap.sprite.set_costume_next(m)
    # if mk == True and key == wrap.K_DOWN:
    #     wrap.sprite.set_costume_prev(m)
