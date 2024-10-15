import random,wrap,time
d=random.randint(0,100)
wrap.world.create_world(1000,1000)
a=random.randint(0,1000)
s=random.randint(500,1000)

# z=random.randint(32,120)
# q=wrap.sprite.get_height()

nomer_tochci=wrap.sprite.add('pacman',a,s,'dot')

time.sleep(random.randint(1,3))

# wrap.actions.move_to(nomer_tochci,random.randint(0,1000),random.randint(0,1000))

poyavlenie_pacmana=random.randint(0,1000)
poyavlenie_pacmana2=random.randint(0,500)

nomer_pacmana=wrap.sprite.add('pacman',poyavlenie_pacmana,poyavlenie_pacmana2,'player1')
z=random.randint(32,120)
wrap.sprite.set_height_proportionally(nomer_pacmana,z)
q=wrap.sprite.get_height(nomer_pacmana)


wrap.actions.set_angle_to_point(nomer_pacmana,a,s)
time.sleep(0.5)
wrap.actions.move_to(nomer_pacmana,a,s)


nomer_prividenie=wrap.sprite.add('pacman',0,0,'enemy_red_right1',False)

w=wrap.sprite.get_height(nomer_prividenie)
e=s-(q//2+w)

nomer_prividenie=wrap.sprite.add('pacman',a,e,'enemy_red_right1')


