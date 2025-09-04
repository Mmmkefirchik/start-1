import  wrap

# from ogon import popatka

wrap.world.create_world(500,500)

# a=wrap.sprite.add('battle_city_items', 250, 250, 'block_bushes')
# b=wrap.sprite.add('battle_city_items', 250, 250, 'block_bushes')
# wrap.sprite.set_size(a,100,100)
# wrap.sprite.set_size(b,100,100)
# wrap.sprite.set_angle(a,60)
# wrap.sprite.set_angle(b,60)

def doroga(ugol,shirina,dlina,otkuda_x,otkuda_y,material_costume,material_spriyta):
    popatka=0
    while popatka<=dlina:
        popatka=popatka+shirina
        b = wrap.sprite.add(material_spriyta, otkuda_x,otkuda_y,material_costume,visible=False)
        wrap.sprite.set_size(b, shirina, shirina)
        wrap.sprite.set_angle(b, ugol)

        wrap.sprite.move_at_angle(b,ugol,-popatka)
        wrap.sprite.show(b)
        # shirina=shirina+shirina
doroga(-60,16,300,100,200,'block_bushes','battle_city_items')

