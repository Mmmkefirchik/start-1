import wrap
from wrap import sprite
#wrap.sprite.set_costume
wrap.world.create_world(400, 600, 900, 50)
# world.set_back_color(100, 200, 200)
tank1= sprite.add("battle_city_tanks", 100, 100, "tank_enemy_size1_green1")
tank2= sprite.add("battle_city_tanks", 200, 300, "tank_enemy_size1_purple2")


def move_left(tank_nomer,x):
    wrap.actions.set_angle_modif(tank_nomer,-90,500)
    wrap.actions.move(tank_nomer,-x,0,900)


def move_down(tank_nomer,y):
    wrap.actions.set_angle_modif(tank_nomer,180,500)
    wrap.actions.move(tank_nomer,0,y,900)

def move_right(tank_nomer,x):
    wrap.actions.set_angle_modif(tank_nomer,90,500)
    wrap.actions.move(tank_nomer,x,0,900)

def move_up(tank_nomer,y):
    wrap.actions.set_angle_modif(tank_nomer,180,500)
    wrap.actions.move(tank_nomer,0,y,500)

move_down(tank1,200)
move_left(tank1,50)
move_right(tank1,200)
move_up(tank1,150)

move_down(tank2,0)
move_left(tank2,150)
move_right(tank2,100)
move_up(tank2,100)

