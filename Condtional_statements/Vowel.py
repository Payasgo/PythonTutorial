#Accept a char from the user findout the given chaar is vowel or con

ch=input("Enter any char :")

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("vowel")
else:
    print("NotVowel")
    
#Second logic
lst=input("Enter any char : ")

lst['a','e','i','o','u','A','E','I','O','U']

if lst in "aeiouAEIOU":
if ch in lst:
    print("Vowel")
else:
    print("NotVowel")
