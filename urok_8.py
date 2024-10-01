import time

import wrap

width=900
height=700

x=50
y=height-50
x1=500
y1=400
x2=600
y2=520
x3=100
y3=300
x4=width/2
y4=height/2

wrap.world.create_world(width,height)

wrap.sprite.add('pacman',50,50,'enemy_blue_down1')
# wrap.actions.move(0,100,100)
# wrap.actions.move_to(0,100,100)
# exit()

wrap.sprite.add('pacman',x,y,'enemy_pink_up1')

wrap.sprite.add('pacman',width-50,height-50,'enemy_ill_white1')

wrap.sprite.add('pacman',width-50,height-height+50,'enemy_red_left1')

wrap.sprite.add('pacman',x1,y1,'dot')

wrap.sprite.add_text('Точка1',x1,y1-25,text_color=[255,255,255])

wrap.sprite.add('pacman',x2,y2,'dot')
wrap.sprite.add_text('Точка3',x2,y2-25,text_color=[255,255,255])

wrap.sprite.add('pacman',x3,y3,'dot')
wrap.sprite.add_text('Точка2',x3,y3-25,text_color=[255,255,255])

wrap.sprite.add('pacman',x4,y4,'player1')
# time.sleep(1.5)
#
# wrap.actions.move_to(10,x1,y1)
# time.sleep(0.2)
#
# wrap.actions.move_to(10,x3,y3)
# time.sleep(0.2)

# wrap.actions.move_to(10,x2,y2)
# time.sleep(0.2)

wrap.actions.move_to(10,x4,y1)
time.sleep(0.5)

wrap.actions.move_to(10,x1,y1)

wrap.actions.move_to(10,x1,y3)
time.sleep(0.5)

wrap.actions.move_to(10,x3,y3)
time.sleep(0.5)

wrap.actions.move_to(10,x3,y2)
time.sleep(0.5)

wrap.actions.move_to(10,x2,y2)



