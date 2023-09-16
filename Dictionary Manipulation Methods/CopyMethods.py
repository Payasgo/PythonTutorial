#D.copy()---->shallow copy of dict
stu = {"sno":101, "sname":"PPM", "Scity":"Hyd"}
print("stu :",stu)

stu2 =stu.copy()
print("stu2",stu)

#D.popitem()----> tuple
t=stu.popitem()
print("Deleting item :", t)
print("dict is:",stu)

#D.pop(k,d=None)--->d
#D.pop(k[,d])---->d----->Keyerror(optional)
values = stu.pop("sname")
print("values of deleted key :", values)
print("After deleting:",stu)

values = stu.pop("sage","XXX")
print("values of deleted key:",values)

#stu.pop("sage")

#D.clear() it will erase all the item form dict collection
stu.clear()
print("stu:",stu)