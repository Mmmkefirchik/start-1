import wrap


w=500
wrap.world.create_world(w,500)
wrap.world.set_back_color(98,149,248)

e = wrap.sprite.add('mario-enemies',1000 , 450, 'cloud')
c = wrap.sprite.get_width(e)

for b in range(c//2,w,c):
    # wrap.sprite.move_to(e,c,0)
    wrap.sprite.add('mario-enemies',b, 450, 'cloud')

q=wrap.sprite.add('mario-scenery',1000,450,'heaven_cloud')
i = wrap.sprite.get_width(q)//2
start=150
for r in range(start, i * 6 + start, i):
    m=wrap.sprite.add('mario-scenery',r, 250, 'heaven_cloud')
    wrap.sprite.set_size_percent(m,50,50)

s=wrap.sprite.add('mario-items',1000,450,'block_bricks')
height_sten=wrap.sprite.get_height(s)
for f in range(100,height_sten*8+100,height_sten):
    wrap.sprite.add('mario-items',100,f,'block_bricks')


m=wrap.sprite.add('mario-items',1000,450,'coin')
width_m=wrap.sprite.get_width(m)
for y in range(width_m,w,width_m*2):
    n=width_m*5
    m = wrap.sprite.add('mario-items', y, 200, 'coin')
    g=wrap.sprite.get_x(m)
    if n == g:
        continue


