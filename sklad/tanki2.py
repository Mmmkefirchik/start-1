import wrap, random

wrap.world.create_world(500, 500)
t_x = random.randint(0, 500)
t_y = random.randint(0, 500)
pos_x = 2
pos_y = 2
t = wrap.sprite.add('battle_city_tanks', t_x, t_y, 'tank_player_size1_green2')
p = wrap.sprite.add('pacman', pos_x, pos_y, 'player2', visible=False)
pr_p = 0


@wrap.always(10000)
def peremechenie():
    t_x = random.randint(0, 500)
    t_y = random.randint(0, 500)
    wrap.sprite.move_to(t, t_x, t_y)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def podmena(pos_x, pos_y):
    p_t=wrap.sprite.is_visible(p)
    if wrap.sprite.is_collide_point(t, pos_x, pos_y) == True or (wrap.sprite.is_collide_sprite(p,t) and p_t==True):
        wrap.sprite.set_costume_next(t)
        wrap.sprite.set_costume_next(t)


@wrap.on_key_down(wrap.K_UP)
def pricel():
    global pr_p
    wrap.sprite.show(p)
    if pr_p != 150:
        pr_p = pr_p + 50

    else:
        wrap.sprite.hide(p)
        pr_p = 0
    wrap.sprite.set_size_percent(p, pr_p, pr_p)


@wrap.on_mouse_move()
def dvizh_p(pos_x, pos_y):
    wrap.sprite.move_to(p, pos_x, pos_y)
    wrap.sprite.set_angle(p, 360)
