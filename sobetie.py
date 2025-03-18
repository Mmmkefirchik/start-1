from symbol import if_stmt

import wrap

wrap.world.create_world(500, 500)

p = wrap.sprite.add('pacman', 250, 250, 'player2')
pr = wrap.sprite.add('pacman', 400, 400, 'enemy_ill_blue1', visible=False)


@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT)
def dvizh(keys):
    if wrap.K_LEFT in keys:
        kooda = wrap.sprite.get_angle(p)
        wrap.sprite.set_angle(p, kooda + 15)
    if wrap.K_RIGHT in keys:
        kooda = wrap.sprite.get_angle(p)
        wrap.sprite.set_angle(p, kooda - 15)


@wrap.on_key_always(wrap.K_UP)
def beg():
    wrap.sprite.move_at_angle_dir(p, 5)


@wrap.on_mouse_move
def mouse(pos_x, pos_y):
    wrap.sprite.move_to(pr, pos_x, pos_y)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def poyavlenie():
    wrap.sprite.show(pr)


@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def ischeznovenie():
    wrap.sprite.hide(pr)

@wrap.always()
def pogonya():
    t_f__pr = wrap.sprite.is_visible(pr)
    pr_x = wrap.sprite.get_x(pr)
    pr_y = wrap.sprite.get_y(pr)
    if t_f__pr == True:
        wrap.sprite.set_angle_to_point(p,pr_x,pr_y)
        wrap.sprite.move_at_angle_point(p, pr_x, pr_y,5)



