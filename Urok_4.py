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
time.sleep(1)
wrap.sprite.add_text('Привет! Да, мы уже тут',700,700)
time.sleep(2)

wrap.sprite.add('mario-items',500,500,'coin')
wrap.sprite.set_size(4,100,100)

time.sleep(1.5)

wrap.sprite.add_text('Привет, меня зовут Коин, и я друг трубы',500,400)
time.sleep(2)
wrap.sprite.add_text('А как тебя зовут?',500,300)
time.sleep(2)

wrap.sprite.add_text('Меня зовут Звездочка, очень приятно',300,600)
time.sleep(2)

wrap.sprite.add_text('Взаимно!',500,200)
time.sleep(2)

wrap.sprite.add_text('Отлично, теперь вы знакомы!',700,600)
time.sleep(2)

wrap.sprite.add_text('А теперь давайте гулять?',700,500)
time.sleep(2)

wrap.sprite.add_text('ВОТ ТАК И ПОЗНОКОМИЛИСЬ КОИН И ЗВЕЗДОЧКА!',500,100)






