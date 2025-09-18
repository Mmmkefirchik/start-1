import  wrap

x=600
wrap.world.create_world(x,600)

shar=wrap.sprite.add('mario-enemies',200,15,'fire_ball',visible=False)
wrap.sprite.set_size_percent(shar,150,150)
shirina_shara=wrap.sprite.get_width(shar)


id_sharov=[]
nomer1=[]
popatka=1
for shag_dlya_shara in range(shirina_shara//2,600,shirina_shara):
    shar=wrap.sprite.add('mario-enemies',shag_dlya_shara,15,'fire_ball')
    id_sharov.append(shar)
    wrap.sprite.set_size_percent(shar,150,150)

    nomer=wrap.sprite.add_text(str(popatka),shag_dlya_shara,15,text_color=(0,0,255))
    popatka=popatka+1
    nomer1.append(nomer)


d=len(id_sharov)
while True:
    for polyot in range(0,d):
        wrap.sprite.move(id_sharov[polyot],0,10)
        wrap.sprite.move(nomer1[polyot],0,10)
