import wrap, random

wrap.world.create_world(500, 500)

a = []
a.append(wrap.sprite.add('pacman', 250, 250, 'enemy_yellow_left1'))
a.append(wrap.sprite.add('pacman', 250, 250, 'item_apple'))
a.append(wrap.sprite.add('pacman', 250, 250, 'player1'))
a.append(wrap.sprite.add('pacman', 250, 250, 'item_strawberry'))
a.append(wrap.sprite.add('pacman', 250, 250, 'item_cherry'))

popatka=0
col_f = []
for sp in a:
    popatka=popatka+1
    print(sp)

    sp_vn = random.randint(10, 490)
    sp_pl = random.randint(10, 240)
    wrap.sprite.move_to(sp, sp_pl, sp_vn)

    sp_sh = random.randint(0, 50)
    sp_v = random.randint(0, 50)
    wrap.sprite.set_size(sp, sp_sh, sp_v)


    sp_koory = wrap.sprite.get_y(sp)
    sp_koorx=wrap.sprite.get_right(sp)
    f=wrap.sprite.add('mario-scenery',sp_koorx,sp_koory, 'firework1')
    col_f.append(f)
    shir_f=wrap.sprite.get_width(f)/2
    wrap.sprite.move(f,shir_f,0)
t=0
while True:
    t = t + 15
    for u in col_f:
        wrap.sprite.set_angle(u, t)
        if wrap.sprite.get_right(u)<500:
            wrap.sprite.move(u,5,0)
        if wrap.sprite.get_right(u)>=500:
            wrap.sprite.move(u,0,5)



