import wrap, time
from wrap_mENdRU.sprite import set_costume

wrap.world.set_back_color(255,225,255)
wrap.world.create_world(1000,1000)
wrap.sprite.add('mario-items',-21,800,'star')
wrap.sprite.set_size(0,100,100)
#wrap.actions.move(0,321,0,3000)
wrap.sprite.move(0,321,0)1
time.sleep(1)
wrap.sprite.add_text('Труба выходи, не бойся',300,700)
time.sleep(1)

wrap.sprite.add('mario-items',-21,800,'pipe')
wrap.sprite.set_size(2,100,100)
wrap.actions.move(2,700,0,3000)
time.sleep(1)
wrap.sprite.add_text('А я и не б-боюсь',675,700)
time.sleep(1)

wrap.sprite.add_text('Так зачем ты меня позвала?',675,650)
time.sleep(1)

wrap.sprite.set_costume(0,'mushroom_liveup')
time.sleep(3)

wrap.sprite.add_text('ХА ХА ХА, ты даже не заметила что я не звездочка!',300,650)
time.sleep(5)

wrap.sprite.add_text('Теперь я сделаю так чтобы ты не смогла пропустить марио на новые уровни!',300,600)
time.sleep(5)

wrap.sprite.add_text('Я сделаю из тебя себе подобного',300,550)
time.sleep(2)

wrap.sprite.add_text('Нет! Не надо!',655,550)
time.sleep(2)

wrap.sprite.set_costume(2,'mushroom_liveup')
time.sleep(3)

wrap.sprite.add_text('ХА ХА ХА! Теперь ты просто моя прислуга',300,500)


