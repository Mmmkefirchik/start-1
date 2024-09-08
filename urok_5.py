import time

import wrap
wrap.world.create_world(1000,1000)
wrap.sprite.add('mario-1-big',300,800,'walk3')
time.sleep(2)
#wrap.sprite.move_to(0,800,800)
wrap.actions.move_to(0,800,800,5000)
wrap.actions.move(0,100,100)
