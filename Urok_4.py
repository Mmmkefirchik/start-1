import  wrap,time
wrap.world.set_back_color(255,255,255)
wrap.world.create_world(1000,1000)
    wrap.sprite.add('mario-items',300,800,'star')
wrap.sprite.set_size(0,100,100)
time.sleep(2)
wrap.sprite.add_text('Привет, вы уже тут?',300,700)
time.sleep(1.8)



wrap.sprite.add('mario-items',700,800,'pipe')
wrap.sprite.set_size(2,100,100)
time.sleep(2)

wrap.sprite.add('mario-items',500,500,'coin')
wrap.sprite.set_size(3,100,100)

time.sleep(1.5)