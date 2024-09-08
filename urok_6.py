import wrap, time
wrap.world.set_back_color(255,225,255)
wrap.world.create_world(1000,1000)

wrap.sprite.add('mario-items',-21,800,'star')
wrap.actions.move(0,321,0,3000)
