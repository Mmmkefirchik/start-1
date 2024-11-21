import wrap,random


wrap.world.create_world(1000,1000)

privedenie_v_x=random.randint(0,900)
privedenie_v_y=random.randint(0,900)

nomer_prividenie=wrap.sprite.add('pacman',privedenie_v_x, privedenie_v_y,'enemy_pink_right2')

dot_v_x=random.randint(0,900)
dot_v_y=random.randint(0,900)
nomer_dot=wrap.sprite.add('pacman',dot_v_x,dot_v_y,'dot')

if dot_v_x>privedenie_v_x:
    wrap.sprite.set_costume(nomer_prividenie,'enemy_pink_right2')

# if privedenie_v_x>dot_v_x:
else:
    wrap.sprite.set_costume(nomer_prividenie,'enemy_pink_left2')

wrap.actions.move_to(nomer_prividenie,dot_v_x,privedenie_v_y)

if dot_v_y<privedenie_v_y:
    wrap.sprite.set_costume(nomer_prividenie,'enemy_pink_up2')

# if privedenie_v_y<dot_v_y:
else:
    wrap.sprite.set_costume(nomer_prividenie,'enemy_pink_down2')

wrap.actions.move_to(nomer_prividenie,dot_v_x,dot_v_y)



