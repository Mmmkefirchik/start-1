import random, wrap,time

from wrap_py import sprite

wrap.world.create_world(1000, 1000)

z_x = random.randint(10, 900)
z_y = random.randint(10, 900)

nomer_s=wrap.sprite.add('battle_city_items', z_x, z_y, 'block_gift_star')
nomer_a=wrap.sprite.add('mario-enemies', 500, 500, 'armadillo_egg')
a = 1
d=1
i = time.time()
e = time.time() - i
e=int(e)
q = wrap.sprite.add_text(str(e), 500, 500, text_color=[255, 255, 255])

while True:
        # i=time.time()
        e=time.time()-i
        e = int(e)

        # print(e)
        # print(d)
        # q=wrap.sprite.add_text(str(e),500,500,text_color=[255,255,255])
        wrap.sprite_text.set_text(q,str(e))

        wrap.sprite.move_at_angle_point(nomer_a,z_x,z_y,6)
        wrap.sprite.set_angle(nomer_a,a)
        a = a + 4

        if sprite.sprites_collide(nomer_s,nomer_a):
            z_x=random.randint(0,900)
            z_y=random.randint(0,900)
            wrap.sprite.move_to(nomer_s,z_x,z_y)
            d = d + 1

            if d==5:
                break