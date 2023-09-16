#D.dict object k-key | d-value
stu = {"sno": 101, "sname" : "Lukas"}
print("stu:",stu)
#D.keys()-->dict_keys |iterable
keys =stu.keys()
print("keys are :", keys)
for k in keys:
    print(k)
#D.values()-->dict_values|iterable 
Values =stu.values()   
print("values:", Values)
for v in Values:
    print(v)
for k in stu.keys():
    print(k, ">>>", stu(keys))