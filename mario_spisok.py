import wrap

wrap.world.create_world(500,500)
wrap.world.set_back_color(98,149,248)

a=[]
e = wrap.sprite.add('mario-enemies',1000 , 450, 'cloud')
c = wrap.sprite.get_width(e)
t=0.5
for b in range(100):
    # wrap.sprite.move_to(e,c,0)
    a.append(wrap.sprite.add('mario-enemies',c*t, 450, 'cloud'))
    t=t+1
