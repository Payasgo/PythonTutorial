#Accept sno from the user print police if sno is 100
#print fire if sno is 101 print medical if sno is 104
#print EMRI if sno is 108 else print invalid service

n=int(input("Enter a Number :"))

if n==100:
    print("Police")
elif n==101:
    print("Fire")
elif n==104:
    print("Medical")
elif n==108:
    print("EMRI")
else:
    print("Invalid Service")
