import time

from wrap import world, sprite, sprite_text, actions


def razgovor(text, h_v):
    text = sprite.add_text(text, sprite.get_x(h_v), sprite.get_top(h_v) - 20)
    time.sleep(0.5)
    sprite.remove(text)


def pobeg(gradus):
    # побег
    razgovor('Бежим', victim)
    actions.set_size_percent(victim, 30, 30, 500)
    actions.set_angle(victim, gradus, 500)
    actions.move_at_angle_dir(victim, 100, 600)
    actions.set_size_percent(victim, 100, 100, 500)


def pogona():
    # погоня
    razgovor('В погоню', hunter)
    actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), 70, 500)


world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 300, 100, "player2")
hunter = sprite.add("pacman", 100, 100, "enemy_blue_right1")

pobeg(180)
pogona()
pobeg(-135)
pogona()
