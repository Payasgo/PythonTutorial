lstn=["Meta","Del"]
lstc=["java","python"]

stu={}

for i in range(0,2):
    k=lstn[i]
    d=lstc[i]
    stu.update({k:d})
    print("stu:",stu)
