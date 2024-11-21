import wrap


width=500
height=1000

wrap.world.create_world(width,height,0,35)
monstr_y=width//2

monstr_x=123#input('где вы хотите создать центрального монстра?')
monstr_x=int(monstr_x)
nomer_prividenie_c=wrap.sprite.add('pacman', monstr_x, monstr_y,'enemy_red_left2')

nomer_prividenie_v=wrap.sprite.add('pacman', monstr_x, 123,'enemy_pink_left2')
wrap.sprite.set_size_percent(nomer_prividenie_v,width_percent=50,height_percent=50)

nomer_prividenie_n=wrap.sprite.add('pacman', monstr_x, 400,'enemy_yellow_left2')
wrap.sprite.set_size_percent(nomer_prividenie_n,width_percent=200,height_percent=200)

nomer_prividenie_c_do_verha=wrap.sprite.get_top(nomer_prividenie_c)
wrap.sprite.move_bottom_to(nomer_prividenie_v,nomer_prividenie_c_do_verha)

nomer_prividenie_c_do_niza=wrap.sprite.get_bottom(nomer_prividenie_c)
wrap.sprite.move_top_to(nomer_prividenie_n,nomer_prividenie_c_do_niza)