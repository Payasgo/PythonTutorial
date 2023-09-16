#without using method dict collection

stu={}
# Adding new items to dict
stu['sno']=101
stu['sname']="Ramesh"
print("dict :", stu)

# updating and existed dict
stu['sname']= "Mark"
print("dict :",stu)

# Reading the value from dict
name=stu['sname']
print("sname :", name)

# Deleting an item from the dict
del stu['sname']
print("dict :", stu)


