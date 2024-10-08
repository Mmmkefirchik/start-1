import wrap,time
width=1000
height=1000
y=600
wrap.world.create_world(height,width)
x1=400
wrap.sprite.add('mario-items',x1,y,'moving_platform1')
x2=500
wrap.sprite.add('mario-items',x2,y,'moving_platform1')

wrap.sprite.add('mario-items',26,y,'moving_platform1')

wrap.sprite.add('mario-items',width-26,y,'moving_platform1')

wrap.sprite.add('mario-enemies',26,y-26,'mushroom_blue')

prizhok1=y-(x1-26)//2
prizhok_v_x=(x1-26)//2+26
wrap.actions.move_to(4,prizhok_v_x,prizhok1)

prizemlenie=y-26
wrap.actions.move_to(4,x1,prizemlenie)

# prizhok_v_x2=(width-26)//2+12

# x=x2//2+x1//2
x=(x2-x1)//2+x1
prizhok=y-(x2-x1)//2
wrap.actions.move_to(4,x,prizhok)

wrap.actions.move_to(4,x2,y-26)

# a=width-26
# s=a//2+x2//2
x_2=(width-26-x2)//2+x2
a=y-(width-26-x2)//2
wrap.actions.move_to(4,x_2,a)

wrap.actions.move_to(4,width-26,y-26)