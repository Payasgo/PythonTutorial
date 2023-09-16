#syntax:print("fromat specifier" %variable)
#print("fromat specifier" %(variable))

sno=65
print("%d" %sno)

sname="Gamer"
print("%s" %sname)


print("sno is %d" %sno)
print("sname is %s" %sname)

print("sno is %d and sname is %s" %(sno,sname))

print("%d and %s" %(sno,sname))

savg=99.9
print("%f" %savg)
print("savg is %f" %savg)
print("savg is %2f" %savg)

print("savg is %f " %(savg))

print("sno is %d and sname is %s and savg is %2f" %(sno,sname,savg))

print("%d,%s,%f" %(sno,sname,savg))
