import wrap

width=1100
height=800

x=50
y=height-50







wrap.world.create_world(width,height)

wrap.sprite.add('pacman',x,y,'enemy_blue_down1')

x=50
y=50

wrap.sprite.add('pacman',x,y,'enemy_pink_up1')


wrap.sprite.add('pacman',width-50,height-50,'enemy_ill_white1')
