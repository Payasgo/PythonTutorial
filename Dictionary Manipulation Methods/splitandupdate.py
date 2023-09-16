s = "meat=23, mark=16"
stu ={}
lst = s.split(",")#[meta=23, mark=16]

for i in lst:
    k,d = i.split("=")#[meta,23]
    stu.update({k:int(d)})
    print("stu",stu)
    