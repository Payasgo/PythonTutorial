#D.items()---->dict_items | iterable
stu = {"sno":101,"sname":"time","scity":"hyd"}
items = stu.items()
print(items)

for t in items:
    k=t[0]
    d=t[1]
    print(k,d,sep='>>>>')

for t in items:
    k,d=t
    print(k,d,sep='>>>>')

for k,d in items:
    print(k,d,sep='>>>>')