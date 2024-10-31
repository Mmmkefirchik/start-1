import random, math

import wrap

width=500
height=1000
wrap.world.create_world(width,height,0,35)

klad_v_x=random.randint(0,width)
klad_v_y=random.randint(height//2,height)
wrap.sprite.add('mario-items',klad_v_x,klad_v_y,'block_question')

nomer_mario=wrap.sprite.add('mario-1-small',klad_v_x-50,klad_v_y-50,'jump')

wrap.sprite.add('pacman',70,70,'dot')


# mario_v_x=input('Куда вы хотите переместить Марио в x?')
# mario_v_y=input('Куда вы хотите переместить Марио в y?')
#
# mario_v_y=int(mario_v_y)
# mario_v_x=int(mario_v_x)
#
# wrap.actions.move_to(nomer_mario,mario_v_x,mario_v_y)

rastoyanie_do_klada=math.sqrt(klad_v_x*klad_v_x+klad_v_y*klad_v_y)

print(rastoyanie_do_klada)