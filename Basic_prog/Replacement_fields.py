#syntax:print("replacement field" . format(variable))

sno=99
print(sno)
print("%d" %sno)

sname="Meta"
print("{}" .format(sname))

print("{}" .format(sno,sname))

print("sno :{} and sname :{}" .format(sno,sname))

# indexbased replacement

print("sno :{1} and sname :{0}" .format(sno,sname))

print("sno is {1} sname is {0} and{0} is manager" .format(sno,sname))

print("sno is {1} sname is {0} and{0} is manager" .format(sname,sno))


#Namebased replacement

print("sno is :{n} and sname is : {na}" .format(n=sno,na=sname))

print("sno is :{n} and sname is :{na} and {na} is manager" .format(n=sno,na=sname))
