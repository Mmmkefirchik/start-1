import random, wrap

from wrap_py import sprite

wrap.world.create_world(1000, 1000)

z_x = random.randint(10, 900)
z_y = random.randint(10, 900)

nomer_s=wrap.sprite.add('battle_city_items', z_x, z_y, 'block_gift_star')
nomer_a=wrap.sprite.add('mario-enemies', 500, 500, 'armadillo_egg')
a = 1

while True:
        # z_x = random.randint(0, 900)
        # z_y = random.randint(0, 900)
        wrap.sprite.move_at_angle_point(nomer_a,z_x,z_y,6)
        wrap.sprite.set_angle(nomer_a,a)
        a = a + 4
        # z_x = random.randint(10, 900)
        # z_y = random.randint(10, 900)

        if sprite.sprites_collide(nomer_s,nomer_a):
            z_x=random.randint(0,900)
            z_y=random.randint(0,900)
            wrap.sprite.move_to(nomer_s,z_x,z_y)