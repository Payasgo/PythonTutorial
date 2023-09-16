#Accept year from the user findout the given yeat is leap or not

Year=int(input("Enter a Year to be checked :"))

#conditional statement
if Year%4==0:
    print("The year is a Leap Year")
else:
    print("The year is not Leap Year")


#conditional Operators
print("The year is a Leap Year") if Year%4==0 else print("The Year is not Leap Year")
