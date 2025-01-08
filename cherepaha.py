import wrap

wrap.world.create_world(1000,1000)
q=501
d=wrap.sprite.add('mario-enemies',50,q,'dragon_stand2')
m=wrap.sprite.add('mario-1-small',950,50,'jump')

wrap.sprite.set_reverse_x(d,True)
wrap.sprite.set_reverse_x(m,True)

while True:
    w=wrap.sprite.get_y(d)

    e=wrap.sprite.move_at_angle_point(d,50,950,6)


    # if w>=950:

    # while  w >= 950:
    wrap.sprite.move_at_angle_point(d, 50, 50, 6)
            # if w>=50:
                # break
