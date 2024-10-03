import wrap,time
width=1000
height=1000
y=800
wrap.world.create_world(height,width)
x1=400
wrap.sprite.add('mario-items',x1,y,'moving_platform1')
x2=500
wrap.sprite.add('mario-items',x2,y,'moving_platform1')

wrap.sprite.add('mario-items',26,y,'moving_platform1')

wrap.sprite.add('mario-items',width-26,y,'moving_platform1')

wrap.sprite.add('mario-enemies',26,y-26,'mushroom_blue')

prizhok=y-100
prizhok_v_x=x1//2+12
wrap.actions.move_to(4,prizhok_v_x,prizhok)

prizemlenie=y-26
wrap.actions.move_to(4,x1,prizemlenie)

prizhok_v_x2=x1+x2//2+12
wrap.actions.move_to(4,prizhok_v_x2,prizhok)

