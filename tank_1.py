import time

import wrap
from wrap import sprite


def zaposk(nomer_tanka):
    wrap.sprite.hide(nomer_tanka)

    x2 = wrap.sprite.get_x(nomer_tanka)
    y2 = wrap.sprite.get_y(nomer_tanka)
    zvezda = sprite.add("battle_city_items", x2, y2, "effect_appearance1")
    time.sleep(0.2)
    wrap.sprite.set_costume(zvezda, 'effect_appearance2')
    time.sleep(0.2)
    wrap.sprite.set_costume(zvezda, 'effect_appearance3')
    time.sleep(0.2)
    wrap.sprite.set_costume(zvezda, 'effect_appearance4')
    time.sleep(0.2)
    wrap.sprite.set_costume(zvezda, 'effect_appearance3')
    time.sleep(0.2)
    wrap.sprite.set_costume(zvezda, 'effect_appearance2')
    time.sleep(0.2)
    wrap.sprite.set_costume(zvezda, 'effect_appearance1')
    wrap.sprite.hide(zvezda)
    time.sleep(0.2)
    wrap.sprite.show(nomer_tanka)

    # sprite.add("battle_city_tanks", 200, 300, "tank_enemy_size1_purple2")

    time.sleep(0.2)


def move_left(tank_nomer, x):
    wrap.actions.set_angle(tank_nomer, -90, 500)
    wrap.actions.move(tank_nomer, -x, 0, 900)


def move_down(tank_nomer, y):
    wrap.actions.set_angle(tank_nomer, 180, 500)
    wrap.actions.move(tank_nomer, 0, y, 900)


def move_right(tank_nomer, x):
    wrap.actions.set_angle(tank_nomer, 90, 500)
    wrap.actions.move(tank_nomer, x, 0, 900)


def move_up(tank_nomer, y):
    wrap.actions.set_angle(tank_nomer, 180, 500)
    wrap.actions.move(tank_nomer, 0, y, 500)

def shot(tank_nomer):
    y1=wrap.sprite.get_y(tank_nomer)
    x1=wrap.sprite.get_x(tank_nomer)

    pola=sprite.add('battle_city_items',x1,y1-25, 'bullet')

    # wrap.actions.move(pola,rasst,0,500)

wrap.world.create_world(400, 600, 900, 50)
tank1 = sprite.add("battle_city_tanks", 100, 300, "tank_enemy_size1_green1")
tank2 = sprite.add("battle_city_tanks", 200, 300, "tank_enemy_size1_purple2")

shot(tank1)
# zvezda = sprite.add("battle_city_items", 500, 500, "effect_appearance1", False)
# zaposk(tank1)
# zaposk(tank2)
#
# move_down(tank1,200)
# move_left(tank1,50)
# move_right(tank1,200)
# move_up(tank1,150)
#
# move_down(tank2, 0)
# move_left(tank2, 150)
# move_right(tank2, 100)
# move_up(tank2, 100)
# zaposk(tank2)
