import wrap,time


wrap.world.create_world(500,500)
wrap.world.set_back_color(96,150,248)

pol=wrap.sprite.add('mario-scenery',2500,250,'ground')
liana=wrap.sprite.add('mario-items',2500,250,'vine2')
piramida=wrap.sprite.add('mario-scenery',2500,250,'block')
shirina_piramidi=wrap.sprite.get_width(piramida)
visota_liani=wrap.sprite.get_height(liana)
shirina_pola=wrap.sprite.get_width(pol)

for stroyka_pola in range(shirina_pola//2,500,shirina_pola):
    wrap.sprite.add('mario-scenery', stroyka_pola,484, 'ground')
    wrap.sprite.add('mario-scenery',stroyka_pola,452,'ground')

for stroyka_liani in range(435-visota_liani//2,0,-visota_liani):
    liana = wrap.sprite.add('mario-items', 400, stroyka_liani, 'vine2')
popatka=0
for f in range(0, 232, 32):
    for stroyka_piramidi in range(shirina_piramidi//2+f,288,shirina_piramidi):
        wrap.sprite.add('mario-scenery', stroyka_piramidi,420-f, 'block')
        time.sleep(0.1)
        # wrap.sprite.add('mario-scenery',stroyka_piramidi+32,436,'block')




