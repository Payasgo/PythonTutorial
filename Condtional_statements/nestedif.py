#Accept gender and age from the user findout the status of the candidate.
    #if gender is m or M then check the age if age>=21then print major else minor
    #if gender is f or F then check the age if age>=18 then print major else minor
    #else print thrid gender

gender=input("Enter any char :")
age=int(input("Enter a number :"))

if gender=='m' or 'M':
    print("Male")
    if age>21:
        print("major")
    else:
        print("minor")
elif gender=='f' or 'F':
    print("Female")
    if age>18:
        print("major")
    else:
        print("minor")
else:
    print("Third gender")
