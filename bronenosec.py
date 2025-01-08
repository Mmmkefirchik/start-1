import random, wrap,time


wrap.world.create_world(1000, 1000)

z_x = random.randint(10, 900)
z_y = random.randint(10, 900)

nomer_s=wrap.sprite.add('battle_city_items', z_x, z_y, 'block_gift_star')
nomer_a=wrap.sprite.add('mario-enemies', 500, 500, 'armadillo_egg')
a = 1
d=1
i = time.time()
e1 = time.time() - i
e1=int(e1)
q = wrap.sprite.add_text(str(e1), 500, 500, text_color=[255, 255, 255])
# nomer_s=q
f=0
e=wrap.sprite.add_text(str(f), 500, 450, text_color=[255, 255, 255])
l=5
while True:

        e1= time.time() - i
        e1 = int(e1)


        wrap.sprite_text.set_text(q, str(e1))
        if e1 == 10:
            break

        u=wrap.sprite.move_at_angle_point(nomer_a,z_x,z_y,l)
        wrap.sprite.set_angle(nomer_a,a)
        a = a + 4
        if wrap.sprite.is_collide_sprite(nomer_s,nomer_a):
            l=l*2
            wrap.sprite_text.set_text(e,str(f))
            f=f+1
            z_x=random.randint(0,900)
            z_y=random.randint(0,900)
            wrap.sprite.move_to(nomer_s,z_x,z_y)
            d = d + 1



