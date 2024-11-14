import wrap


width=500
height=1000

wrap.world.create_world(width,height,0,35)

monstr_y=width//2

monstr_x=123#input('где вы хотите создать центрального монстра?')
monstr_x=int(monstr_x)

nomer_prividenie_c=wrap.sprite.add('pacman', monstr_x, monstr_y,'enemy_red_left2')

monstrv_y=wrap.sprite.move_top_to()

nomer_prividenie_v=wrap.sprite.add('pacman', monstr_x, monstr_y,'enemy_pink_left2')

top=wrap.sprite.set_size_percent(nomer_prividenie_c,50,50)
