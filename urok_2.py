from time import sleep

import  wrap,time
wrap.world.create_world(1000,1000)
wrap.sprite.add('mario-items',300,800,'star')
wrap.sprite.add('mario-items',700,800,'pipe')
wrap.sprite.set_size(0,100,100)
wrap.sprite.set_size(1,100,100)



wrap.sprite.add_text('Привет, как дела?',300,700)
wrap.world.set_back_color(255,255,255)

time.sleep(1.5)
wrap.sprite.add_text('Привет, все хорошо',700,700)

time.sleep(1.5)
wrap.sprite.add_text('Что ты сегодня делала утром?? ',300,650)
time.sleep(2)
wrap.sprite.add_text('Я освещяла Марио дорогу!',300,600)
time.sleep(1.8)

wrap.sprite.add_text('Прикольно, а я его на новые уровни пропускала ',700,600)
time.sleep(2)
wrap.sprite.add_text('У тебя сегодня есть свободное время?',700,550)
time.sleep(1.5)
wrap.sprite.add_text('Если есть, то можно встретится погулять',700,500)
time.sleep(1.5)
wrap.sprite.add_text('У меня есть после обеда',700,450)

time.sleep(1.5)
wrap.sprite.add_text('О, круто! у меня тоже после обеда',300,450)
time.sleep(1.8)
wrap.sprite.add_text('Где встретимся?',300,400)
time.sleep(2)
wrap.sprite.add_text('Я предлагаю у последнего уровня!',300,350)

time.sleep(2)
wrap.sprite.add_text('Договорились',700,350)
time.sleep(1.5)
wrap.sprite.add_text('Я уще приведу своего друга, пока',700,300)

time.sleep(2)
wrap.sprite.add_text('Хорошо, счастливо!',300,300)











