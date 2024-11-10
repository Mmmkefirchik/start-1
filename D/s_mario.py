import random, math, wrap


width=500
height=1000
wrap.world.create_world(width,height,0,35)

klad_v_x=random.randint(0,width)
klad_v_y=random.randint(height//2,height)
wrap.sprite.add('mario-items',klad_v_x,klad_v_y,'block_question')

nomer_mario=wrap.sprite.add('mario-1-small',70, 70, 'jump')

wrap.sprite.add('pacman',70,70,'dot')


# mario_v_x=input('Куда вы хотите переместить Марио в x?')
# mario_v_y=input('Куда вы хотите переместить Марио в y?')
#
# mario_v_y=int(mario_v_y)
# mario_v_x=int(mario_v_x)''''''''''''''''''''''''''''

# wrap.actions.move_to(nomer_mario,mario_v_x,mario_v_y)

katet_1y=klad_v_y-70
katet_1x=klad_v_x-70

rastoyanie_do_klada=math.sqrt(katet_1y*katet_1y+katet_1x*katet_1x)

i=int(rastoyanie_do_klada)
s=str(i)

wrap.sprite.add_text('Да клада '+ s +' px',70,35,text_color=[255,255,255])

