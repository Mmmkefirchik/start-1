import wrap,time,random
wrap.world.create_world(500,500)

a=range(100)
e=[]
costume=['green','white','yellow','purple']
for r in a:
    coor_x=random.randint(0,500)
    coor_y=random.randint(0,500)
    f=wrap.sprite.add('battle_city_tanks',coor_x,coor_y,'tank_enemy_size1_green1')
    e.append(f)

    vibor_cost=f'tank_enemy_size{random.randint(1,4)}_{random.choice(costume)}1'
    wrap.sprite.set_costume(f,vibor_cost)

