import random,wrap,time

d=random.randint(0,100)
wrap.world.create_world(1000,1000)
mesto_tochci_x=random.randint(0, 1000)
mesto_tochci_y=random.randint(500, 1000)


nomer_tochci=wrap.sprite.add('pacman', mesto_tochci_x, mesto_tochci_y, 'dot')

time.sleep(random.randint(1,3))

poyavlenie_pacmana_x=random.randint(300, 700)
poyavlenie_pacmana_y=random.randint(0, 500)

nomer_pacmana=wrap.sprite.add('pacman', poyavlenie_pacmana_x, poyavlenie_pacmana_y, 'player1')
rasmer_pacman=random.randint(32, 120)
wrap.sprite.set_height_proportionally(nomer_pacmana, rasmer_pacman)
height_pacman=wrap.sprite.get_height(nomer_pacmana)

wrap.actions.set_angle_to_point(nomer_pacmana, mesto_tochci_x, mesto_tochci_y)
time.sleep(0.5)
wrap.actions.move_to(nomer_pacmana, mesto_tochci_x, mesto_tochci_y)

rasmer_privideniya=random.randint(32, 300)
nomer_prividenie=wrap.sprite.add('pacman',0,0,'enemy_red_right1',False)

mesto_privideniya_y=mesto_tochci_y-height_pacman//2-20-rasmer_privideniya//2

mesto_privideniya_x=random.randint(mesto_tochci_x-50,mesto_tochci_x+50)

nomer_prividenie=wrap.sprite.add('pacman', mesto_privideniya_x, mesto_privideniya_y, 'enemy_red_right1')
# rasmer_privideniya=random.randint(300, 300)
wrap.sprite.set_height_proportionally(nomer_prividenie, rasmer_privideniya)
height_prividenie=wrap.sprite.get_height(nomer_prividenie)

mesto_texta_y= mesto_privideniya_y - (height_prividenie // 2 + 20)

wrap.sprite.add_text('Ага, попался!', mesto_privideniya_x, mesto_texta_y, text_color=[255, 255, 255])


gradys_privedenie=wrap.sprite.calc_angle_by_point(nomer_pacmana,mesto_privideniya_x,mesto_privideniya_y)
gradys_pacman=gradys_privedenie-180

wrap.actions.set_angle(nomer_pacmana,gradys_pacman)


wrap.actions.move_at_angle_dir(nomer_pacmana,100)