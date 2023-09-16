#Accept String from the user findout no.of.caps no.of.small no.of.digits in the given String iff the give String alpanumeric

data=input("Enterr a number :")
if data.isalnum():
    print("Yes it is alnum")
    nc=ns=nd=0
    for i in data:
        if i.isupper():
            nc=nc+1
        elif i.isdigit:
            nd=nd+1
        elif i.islower():
            ns=ns+1
        print("no of cap",nc)
        print("no of dig",nd)
        print("no of low",ns)
