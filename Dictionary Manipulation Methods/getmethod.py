#D.get(k,d=None)------>d

stu = {"sno":101, "sname":"Meta"}
print("stu:",stu)

v=stu['sname']
print("value is :", v)

v=stu.get('sname')
print("value is :", v)

v=stu.get("scity")
print("value is :",v)

v=stu.get("scity","hyd")
print("value is ;", v)
