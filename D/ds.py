import wrap,random, math

wrap.world.create_world(1000,1000)

mesto_tochci1_x=random.randint(70, 70)
mesto_tochci1_y=random.randint(70, 70)

wrap.sprite.add('pacman', mesto_tochci1_x, mesto_tochci1_y,'dot')

mesto_tochci2_x=random.randint(170,170)
mesto_tochci2_y=random.randint(170,170)

wrap.sprite.add('pacman', mesto_tochci2_x, mesto_tochci2_y,'dot')

katet_y=mesto_tochci2_y-mesto_tochci1_y
katet_x=mesto_tochci2_x-mesto_tochci1_x

rastoyanie_ot_dot_do_dot=math.sqrt(katet_y*katet_y+katet_x*katet_x)



print(rastoyanie_ot_dot_do_dot)


