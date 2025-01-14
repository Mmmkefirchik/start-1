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
p=False
# p=wrap.sprite.add('mario-enemies', 6, 500, 'fire_stream',p)
coordinat_dino_y = wrap.sprite.get_y(d)
coordinat_dino_x = wrap.sprite.get_y(d)
time2 = time.time() - i
time2 = int(time2)


u=wrap.sprite.add('mario-enemies', coordinat_dino_x, coordinat_dino_y, 'fire_stream',p)

while True:

    time1 = time.time() - i
    time1 = int(time1)
    time_do_vistrela = time.time() - o
    if int(time_do_vistrela)==5:
        wrap.sprite.add('mario-enemies',500,coordinat_dino_y, 'fire_stream')
        o=time.time()
    wrap.sprite_text.set_text(nomer_t, str(time1))
    wrap.sprite_text.set_text(nomer_t2,str(int(time_do_vistrela)))

    # Dino
    coordinat_dino_y = wrap.sprite.get_y(d)
    coordinat_dino_x = wrap.sprite.get_y(d)

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

    # if e1%5==0 and e1!=0:
    #     wrap.sprite.add('mario-enemies',coordinat_dino_x,coordinat_dino_y, 'fire_stream', p)
    # o = wrap.sprite.add('mario-enemies', 100, 100, 'fire_stream', p)
    u = wrap.sprite.add('mario-enemies', 500, coordinat_dino_y, 'fire_stream',p)


    #     p=True
    #     wrap.sprite.move_to(u,500,coordinat_dino_y)
    # if float(r1)%5==0 and float(r1)==0:
    #     p=False
    #     p=wrap.sprite.add('mario-enemies',coordinat_dino_x, coordinat_dino_y, 'fire_stream',True)
    #     wrap.sprite.set_add(p,)
    #     p=True
    # if e1%5!=0:
    #     p=False






