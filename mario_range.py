import wrap,time


wrap.world.create_world(500,500)
wrap.world.set_back_color(96,150,248)

pol=wrap.sprite.add('mario-scenery',2500,250,'ground')
shirina_pola=wrap.sprite.get_width(pol)

stupenki=wrap.sprite.add('mario-items',2500,250,'moving_platform1')
shirina_stupenki=wrap.sprite.get_width(stupenki)

liana=wrap.sprite.add('mario-items',2500,250,'vine2')
visota_liani=wrap.sprite.get_height(liana)

piramida=wrap.sprite.add('mario-scenery',2500,250,'block')
shirina_piramidi=wrap.sprite.get_width(piramida)

for stroyka_pola in range(shirina_pola//2,500,shirina_pola):
    wrap.sprite.add('mario-scenery', stroyka_pola,484, 'ground')
    wrap.sprite.add('mario-scenery',stroyka_pola,452,'ground')

for stroyka_liani in range(435-visota_liani//2,0,-visota_liani):
    liana = wrap.sprite.add('mario-items', 400, stroyka_liani, 'vine2')
popatka=0
for f in range(0, 232, 32):
    for stroyka_piramidi in range(shirina_piramidi//2+f,288,shirina_piramidi):
        wrap.sprite.add('mario-scenery', stroyka_piramidi,422-f, 'block')
        # wrap.sprite.add('mario-scenery',stroyka_piramidi+32,436,'block')


for shirina_stupenki in range(200,0,-shirina_stupenki):
    stupenki = wrap.sprite.add('mario-items',shirina_stupenki,shirina_stupenki//2+30, 'moving_platform1')





