#Accept a char from the user print male iff the given char is m or M else print Female

ch=input("Enter any char :")

#Conditional statement
if ch=='m' or ch=='M':
    print("Male")
else:
    print("Female")

#Conditional operator
print("Male") if ch=='m'or ch=='M' else print("Female")
