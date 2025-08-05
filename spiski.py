import  random
# a=[1,2,3]
# a.append('hdjh')
# a.insert(1,9)
# print(a)
a=[]
a.append(random.randint(0,10))
a.append(random.randint(0,10))
a.append(random.randint(1,10))
print(a)

b=[]
b.append(random.randint(0,10))
b.append(random.randint(0,10))
b.append(random.randint(0,10))

print(b)
e=0
d=0


if a[0]>b[0]:
    c='a'
    d=d+1
if b[0]>a[0]:
    c='b'
    e=e+1
if a[0]==b[0]:
    c='ничья'
print('В первом тайме победила команда '+ c)


if a[1]>b[1]:
    c='a'
    d=d+1
if b[1] > a[1]:
    c='b'
    e=e+1
if a[1]==b[1]:
    c='ничья'
print('В втором тайме победила команда '+ c)


if a[2]>b[2]:
    c='a'
    d=d+1
if b[2] > a[2]:
    c='b'
    e=e+1
if a[2]==b[2]:
    c='ничья'
print('В третьем тайме победила команда '+ c)





# if a[2]==b[2] and a[1]==b[1] and a[0]==b[0] or (a[2]==b[2] or a[1]==b[1] or a[0]==b[0]):
#     print('Во всей игре победила ничья')
#
# elif e>d:
#     print('Во всей игре победила команда: '+str('b'))
# elif d>e:
#     print('Во всей игре победила команда: '+str('a'))
if e==d:
    print('Во всей игре победила ничья')
if e>d:
    print('Во всей игре победила команда: '+str('b'))
if d>e:
    print('Во всей игре победила команда: '+str('a'))








