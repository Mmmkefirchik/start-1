import random, math, wrap


width=500
height=1000
wrap.world.create_world(width,height,0,35)

klad_v_x=random.randint(0,width)
klad_v_y=random.randint(height//2,height)
nomer_klada=wrap.sprite.add('mario-items',klad_v_x,klad_v_y,'block_question', False)

nomer_mario=wrap.sprite.add('mario-1-small',70, 70, 'jump')

wrap.sprite.add('pacman',70,70,'dot')

katet_1y=klad_v_y-70
katet_1x=klad_v_x-70

rastoyanie_do_klada=math.sqrt(katet_1y*katet_1y+katet_1x*katet_1x)

i=str (int(rastoyanie_do_klada))

wrap.sprite.add_text('До клада '+ i +' px',70,35,text_color=[255,255,255])

wrap.actions.set_angle_to_point(nomer_mario, klad_v_x, klad_v_y)

mario_v_x=input('Куда вы хотите переместить Марио в x?')
mario_v_y=input('Куда вы хотите переместить Марио в y?')

mario_v_y=int(mario_v_y)
mario_v_x=int(mario_v_x)

wrap.actions.move_to(nomer_mario, mario_v_x, mario_v_y)

wrap.sprite.add('pacman',mario_v_x,mario_v_y,'dot')

katet_1y=klad_v_y-mario_v_y
katet_1x=klad_v_x-mario_v_x

rastoyanie_do_klada=math.sqrt(katet_1y*katet_1y+katet_1x*katet_1x)
i=str (int(rastoyanie_do_klada))
wrap.sprite.add_text('До клада '+ i +' px',mario_v_x,mario_v_y-35,text_color=[255,255,255])

wrap.actions.set_angle_to_point(nomer_mario, klad_v_x, klad_v_y)

mario_v_x=input('Куда вы хотите переместить Марио в x?')
mario_v_y=input('Куда вы хотите переместить Марио в y?')

mario_v_y=int(mario_v_y)
mario_v_x=int(mario_v_x)

wrap.actions.move_to(nomer_mario, mario_v_x, mario_v_y)

katet_1y=klad_v_y-mario_v_y
katet_1x=klad_v_x-mario_v_x

rastoyanie_do_klada=math.sqrt(katet_1y*katet_1y+katet_1x*katet_1x)

i=str (int(rastoyanie_do_klada))
wrap.actions.set_angle_to_point(nomer_mario, klad_v_x, klad_v_y)

wrap.sprite.add_text('До клада '+ i +' px',mario_v_x,mario_v_y-35,text_color=[255,255,255])

wrap.sprite.show(nomer_klada)

print(klad_v_x, klad_v_y)