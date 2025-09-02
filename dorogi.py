import wrap

wrap.world.create_world(450,500)

d1=wrap.sprite.add('mario-items',1000,450,'block_bricks')
shir_d1=wrap.sprite.get_width(d1)
# for d1_x in range(16,18):
# for d1_x in range(shir_d1//2,200,shir_d1+10):
    # wrap.sprite.add('battle_city_items',(d1_x+d1_x-6),50,'block_snow')
    # wrap.sprite.add('mario-items', d1_x, 50, 'block_bricks')
    # wrap.sprite.add('mario-items', (d1_x+d1_x-6+d1_x+d1_x), 50, 'block_bricks')
    # k=wrap.sprite.add('battle_city_items',(d1_x+d1_x-6+d1_x+d1_x+d1_x+d1_x),50,'block_bushes')
    # wrap.sprite.set_size_percent(k,200,200)
#
w=wrap.sprite.add('mario-items', 1000, 450, 'block_bricks')
q=wrap.sprite.get_width(w)
for a in range(q//2,500,q+74):
    wrap.sprite.add('mario-items', a, 16, 'block_bricks')
    wrap.sprite.add('battle_city_items',a+32,16,'block_snow')
    wrap.sprite.add('mario-items', a+42, 16, 'block_bricks')
    k=wrap.sprite.add('battle_city_items',a+74,16,'block_bushes')
    wrap.sprite.set_size_percent(k,200,200)
    wrap.sprite.add('mario-items', a, 16, 'block_bricks')

for b in range(q//2,500,q):
    s_d=wrap.sprite.add('battle_city_items',37,b,'block_snow')
    wrap.sprite.set_width(s_d,10)








