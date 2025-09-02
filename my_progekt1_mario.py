import wrap
from wrap_py import sprite

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
start=300
n=0
# for r in range(start, i * 6 + start, i):
#     m=wrap.sprite.add('mario-scenery',r, 300, 'heaven_cloud')
#     wrap.sprite.set_size_percent(m,50,50)
#     if n==0:
#         n=1


s=wrap.sprite.add('mario-items',1000,450,'block_bricks')
height_sten=wrap.sprite.get_height(s)
for f in range(5,height_sten*8+180,height_sten):
    a=wrap.sprite.add('mario-items',100,f,'block_bricks')



m=wrap.sprite.add('mario-items',1000,450,'coin')
width_m=wrap.sprite.get_width(m)
nomera_monet=[]
for y in range(width_m,w,width_m*2):
    if y==width_m+width_m*2*2 or y==width_m+width_m*2*3:
        continue
    m = wrap.sprite.add('mario-items', y, 200, 'coin')
    nomera_monet.append(m)



mar=wrap.sprite.add('mario-1-small',300,275,'jump')
plot=wrap.sprite.add('mario-scenery',300,300,'cloud1')
wrap.sprite.set_reverse_y(plot,True)
@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def peredviszenie_x(keys):
    pol_x=wrap.sprite.get_x(plot)
    pol_y=wrap.sprite.get_y(plot)-25
    if wrap.sprite.get_left(plot)>100 and wrap.sprite.get_left(plot)<=120:
        wrap.sprite.move_to(plot,0,300)
        wrap.sprite.move_to(mar,pol_x,pol_y)
        return

    if wrap.K_LEFT in keys:
        wrap.sprite.set_reverse_x(mar,True)
        wrap.sprite.move(plot,-5,0)
        wrap.sprite.move_to(mar,pol_x,pol_y)
    if wrap.K_RIGHT in keys:
        wrap.sprite.set_reverse_x(mar,False)
        wrap.sprite.move(plot,5,0)
        wrap.sprite.move_to(mar,pol_x,pol_y)


@wrap.on_key_always(wrap.K_UP,wrap.K_DOWN,wrap.K_SPACE)
def peredviszenie_y(keys):
    pol_x=wrap.sprite.get_x(plot)
    pol_y=wrap.sprite.get_y(plot)-25
    if wrap.sprite.get_bottom(plot)>=434:
        wrap.sprite.move(plot,0,-1)
        return
    if wrap.sprite.get_y(plot)<=266:
        wrap.sprite.move(plot,0,1)
        return

    if wrap.K_UP in keys:
        wrap.sprite.move(plot,0,-5)
        wrap.sprite.move_to(mar,pol_x,pol_y)

    if wrap.K_DOWN in keys:
        wrap.sprite.move(plot,0,5)
        wrap.sprite.move_to(mar,pol_x,pol_y)


@wrap.on_key_down(wrap.K_SPACE)
def priszok(keys):
        wrap.actions.move(mar,0,-50,500)
        for b in nomera_monet.copy():
            if wrap.sprite.is_collide_sprite(mar, b) == True:
                wrap.sprite.remove(b)
                nomera_monet.remove(b)

        wrap.actions.move(mar,0,50,500)














