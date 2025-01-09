import wrap,time

wrap.world.create_world(1000,1000)
q=500
d=wrap.sprite.add('mario-enemies',50,q,'dragon_stand2')
m=wrap.sprite.add('mario-1-small',950,q,'jump')
wrap.sprite.set_reverse_x(d,True)
wrap.sprite.set_reverse_x(m,True)
nomer_t=wrap.sprite.add_text('0', 500, 450, text_color=[255, 255, 255])

speed_dino=5
speed_mar=-5
i = time.time()
e1 = time.time() - i
e1 = int(e1)
while True:#
    e1 = time.time() - i
    e1 = int(e1)
    wrap.sprite_text.set_text(nomer_t,str(e1))

    # Dino
    coordinat_dino = wrap.sprite.get_y(d)

    if coordinat_dino<=50:
        speed_dino=5
    if coordinat_dino>=950:
        speed_dino=-5
    wrap.sprite.move(d, 0, speed_dino)

    # Mar
    coordinat_mar = wrap.sprite.get_y(m)

    if coordinat_mar <= 50:
        speed_mar = 5
    if coordinat_mar >= 950:
        speed_mar = -5
    wrap.sprite.move(m, 0, speed_mar)
