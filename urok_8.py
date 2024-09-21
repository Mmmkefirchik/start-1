import wrap

width=900
height=700

x=50
y=height-50

wrap.world.create_world(width,height)

wrap.sprite.add('pacman',x,y,'enemy_blue_down1')

x=50
y=50

wrap.sprite.add('pacman',x,y,'enemy_pink_up1')

wrap.sprite.add('pacman',width-50,height-50,'enemy_ill_white1')

wrap.sprite.add('pacman',width-50,height-height+50,'enemy_red_left1')

q=width-300
w=height-180
wrap.sprite.add('pacman',q,w,'dot')

a=width-width+300
b=height-180
wrap.sprite.add('pacman',a,b,'dot')

e=width-width+500
r=height-height+100
wrap.sprite.add('pacman',e,r,'dot')
