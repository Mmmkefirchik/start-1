import  random
# a=[1,2,3]
# a.append('hdjh')
# a.insert(1,9)
# print(a)
a=[]
a.append(random.randint(1,10))
a.append(random.randint(1,10))
a.append(random.randint(1,10))
print(a)

b=[]
b.append(random.randint(1,10))
b.append(random.randint(1,10))
b.append(random.randint(1,10))
print(b)
e=0
d=0
if a[0]>b[0]:
    c='a'
    d=d+1
else:
    c='b'
    e=e+1
if a[0]==b[0]:
    c='ничья'
print('В первом тайме победила команда '+ c)

if a[1]>b[1]:
    c='a'
    d=d+1
else:
    c='b'
    e=e+1
if a[1]==b[1]:
    c='ничья'
print('В втором тайме победила команда '+ c)

if a[2]>b[2]:
    c='a'
    d=d+1
else:
    c='b'
    e=e+1
if a[2]==b[2]:
    c='ничья'
print('В третьем тайме победила команда '+ c)

if e>d:
    print('Во всей игре победила команда: '+str(b))
else:

    print('Во всей игре победила команда: '+str(a))


