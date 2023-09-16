import collections
stu =dict()
#stu=collections.orderdDict()
stu.update({"sno":101})
stu.update({"sname":"Meta"})
stu.update({"scity":"hyd"})

for k,d in stu.items():
    print(k,">>>>",d)