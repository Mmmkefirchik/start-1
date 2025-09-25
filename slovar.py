# a={1:2,'f':'k',7:'l'}
#
# a[0]=100
# del a
# print(a)


matvey={'imya':'matvey','ves':53,'vozrast':12}
misha={'imya':'misha','ves':60,'vozrast':14}
ilya={'imya':'ilya','ves':50,'vozrast':13}

sportiki=[matvey,misha,ilya]

vitya={'imya':'vitya','ves':49,'vozrast':12}
sportiki.append(vitya)

for a in sportiki:
    print(a['imya'],a['vozrast'])

for a in sportiki:
    a['vozrast']+=1

for a in sportiki:
    print(a['imya'],a['vozrast'])

for a in sportiki:
    a['god']=2025-a['vozrast']
    del a['vozrast']
print(sportiki)
