import wrap,time,random
wrap.world.create_world(500,500)

a=range(100)
e=[]
for r in a:
    coor_x=random.randint(0,500)
    coor_y=random.randint(0,500)
    e.append(wrap.sprite.add('battle_city_tanks',coor_x,coor_y,'tank_enemy_size1_green1'))
    y=random.choice(e)
    wrap.sprite.set_costume_next(y)

