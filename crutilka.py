import  wrap,random


wrap.world.create_world(500,500)

p=wrap.sprite.add('pacman',250,200,'enemy_blue_down2')
m=wrap.sprite.add('mario-1-big',250,200,'stand')
t=wrap.sprite.add('battle_city_tanks',250,200,'tank_enemy_size1_green1')
cooda=95

def sozd_zcertv(pos_x,pos_y):
    pk = wrap.sprite.is_collide_point(p, pos_x, pos_y)
    mk = wrap.sprite.is_collide_point(m, pos_x, pos_y)
    tk = wrap.sprite.is_collide_point(t, pos_x, pos_y)
    # zhertva=None
    # if zhertva==None :
    if tk==True:
        zhertva = t
    elif mk == True:
        zhertva = m
    elif pk == True:
        zhertva = p
    else:
        zhertva=None
    return zhertva


@wrap.on_key_down(wrap.K_UP,wrap.K_DOWN)
def smena(pos_x,pos_y,key):
    zhertva=sozd_zcertv(pos_x,pos_y)

    if zhertva!=None:
        if key==wrap.K_UP:
            wrap.sprite.set_costume_next(zhertva)
        if key==wrap.K_DOWN:
            wrap.sprite.set_costume_prev(zhertva)


@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def povorot(pos_x,pos_y,keys):
    zhertva=sozd_zcertv(pos_x,pos_y)
    if zhertva!=None:
        u = wrap.sprite.get_angle(zhertva)
        if wrap.K_LEFT in keys:
            wrap.sprite.set_angle(zhertva,u-5)

        if wrap.K_RIGHT in keys:
            wrap.sprite.set_angle(zhertva,u+5)


@wrap.on_mouse_down(wrap.BUTTON_WHEELDOWN,wrap.BUTTON_WHEELUP)
def razmer(pos_x,pos_y,button):
    zhertva=sozd_zcertv(pos_x,pos_y)
    if zhertva!=None:
        x,y=wrap.sprite.get_size_percent(zhertva)
        if button==wrap.BUTTON_WHEELUP:
            wrap.sprite.set_size_percent(zhertva,x+5,y+5)

        if button==wrap.BUTTON_WHEELDOWN:
                wrap.sprite.set_size_percent(zhertva,x-5,y-5)

