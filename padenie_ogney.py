import  wrap

x=600
wrap.world.create_world(x,600)

shar=wrap.sprite.add('mario-enemies',200,15,'fire_ball',visible=False)
wrap.sprite.set_size_percent(shar,150,150)
shirina_shara=wrap.sprite.get_width(shar)

nomera=[*range(1,600//shirina_shara+1)]
for shag_dlya_shara in range(shirina_shara//2,600,shirina_shara):
    shar=wrap.sprite.add('mario-enemies',shag_dlya_shara,15,'fire_ball')
    wrap.sprite.set_size_percent(shar,150,150)

    if len(nomera)!=0:
        wrap.sprite.add_text(str(nomera[0]),shag_dlya_shara,15,text_color=(0,0,255))
        del nomera[0]

