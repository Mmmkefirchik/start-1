import wrap,time

wrap.world.create_world(1000,1000)
q=500
d=wrap.sprite.add('mario-enemies',50,q,'dragon_stand2')
m=wrap.sprite.add('mario-1-small',950,q,'jump')
wrap.sprite.set_reverse_x(d,True)
wrap.sprite.set_reverse_x(m,True)
nomer_t=wrap.sprite.add_text('0', 500, 450, text_color=[255, 255, 255])
nomer_t2=wrap.sprite.add_text('0', 500, 400, text_color=[255, 255, 255])

speed_dino=6
speed_mar=-5
i = time.time()
o=time.time()
time1 = time.time() - i
time1 = int(time1)

coordinat_dino_y = wrap.sprite.get_y(d)
time2 = time.time() - i
time2 = int(time2)

a=2
fire=None
fire_y=None
while True:
    #     fire:
    h=wrap.sprite.get_right(d)
    time1 = time.time() - i
    time1 = int(time1)
    time_do_vistrela = time.time() - o

    if int(time_do_vistrela)==5:

        fire=wrap.sprite.add('mario-enemies',d+100,coordinat_dino_y-3, 'fire_stream')
        m_y = wrap.sprite.get_y(m)
        m_x = wrap.sprite.get_x(m)

        wrap.sprite.move_left_to(fire,h+5)
        o=time.time()
        wrap.sprite.set_angle_to_point(fire, m_x, m_y)

        fire_ugol = wrap.sprite.get_angle(fire)
        wrap.sprite.set_angle(fire, fire_ugol + 180)

        # m_y=wrap.sprite.get_y(m)
        # m_x=wrap.sprite.get_x(m)
    if fire!=None:
        # wrap.sprite.set_angle_modif(fire, 180)
        wrap.sprite.move_at_angle_point(fire,m_x, m_y,50)
        # if
        # wrap.sprite.set_angle(fire,)


    wrap.sprite_text.set_text(nomer_t, str(time1))
    wrap.sprite_text.set_text(nomer_t2,str(int(time_do_vistrela)))


    # Dino
    coordinat_dino_y = wrap.sprite.get_y(d)

    if coordinat_dino_y<=50:
        speed_dino=5
    if coordinat_dino_y>=950:
        speed_dino=-5
    wrap.sprite.move(d, 0, speed_dino)

    # Mar
    coordinat_mar = wrap.sprite.get_y(m)

    if coordinat_mar <= 50:
        speed_mar = 5
    if coordinat_mar >= 950:
        speed_mar = -5
    wrap.sprite.move(m, 0, speed_mar)
    f=wrap.sprite.get_y(d)

    m_y = wrap.sprite.get_y(m)
    m_x = wrap.sprite.get_x(m)

    if fire!=None:
        fire_y = wrap.sprite.get_y(fire)
        f_m=wrap.sprite.is_collide_sprite(fire,m)
        if f_m==True:
            # print(fire_y,m_y)
            break
while m_y!=1000:

    wrap.sprite.set_angle(m, a)
    a=a+5

    m_y = wrap.sprite.get_y(m)
    m_x = wrap.sprite.get_x(m)
    if m_y<800:
        wrap.sprite.move(m, 0, 9)







