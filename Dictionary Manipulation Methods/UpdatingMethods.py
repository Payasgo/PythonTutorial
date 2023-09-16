#D.update({k:d})

stu={}
k=input("Enter keys :")
d=input("Enter values :")

stu.update({k:d})
print("stu :", stu)

stu={}
for i in range (1,4):
    k=input("Enter keys :")
    d=input("Enter values :")
    stu.update({k:d})
    print("stu:",stu)

Stu={"sno" : 101, "sname" : "Lookup"}
print("stu:",stu)

stu.update({"sname": "Meta"})
print("After update", stu)

d1={"sno": 101}
d2={"sname":"Mera"}
#d3=d1+d2--->Error We cannot concentation
print("d1",d1)
print("d2",d2)
d1.update(d1)
print("Result is",d1)
