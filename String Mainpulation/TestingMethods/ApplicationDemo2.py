#Accept a string from the user findout no.of.cap,no.of.small,
#no.of.digit,no.of.spaces,no.of.sym in the given string

data=input("Enter a charcter :")
if data.isalnum():
    print("yes it is alnum")
    nc=ns=nd=nsp=nsy=0
    if i.isalnum():
        nc=nc+1
    elif i.islower():
        ns=ns+1
    elif i.isdigit():
        nd=nd+1
    elif i.isspace():
        nsp=nsp+1
    else:
        nsy=nsy+1

    print("no of cap :", nc)
    print("no of low :", ns)
    print("no of dig :", nd)
    print("no of space:", nsp)
    print("no of sysmbol :", nsy)
