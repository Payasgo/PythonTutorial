# Syntax: print(val,val2,va3......valn, sep=' ', end='\n')
X=120
Y=25.32
Z="Meta_Data"

print(X)
print(Y)
print(Z)

print(X,Y,Z)


print(X,Y,Z, sep='\n')
print(X,Y,Z, sep='\n',end='\n')
print(X,"\n",Y,"\n",Z,"\n")

print(X,Y,Z, sep='\t')
print(X,Y,Z, sep='\t',end='\t')
print(X,"\t",Y,"\t",Z,"\t")


print(X,Y,Z, sep='\a')
print(X,Y,Z, sep='\a',end='\a')
print(X,"\a",Y,"\a",Z,"\a")


print(X,Y,Z, sep='\b')
print(X,Y,Z, sep='\b',end='\b')
print(X,"\b",Y,"\b",Z,"\b")


print(X,Y,Z, sep='\'')
print(X,Y,Z, sep='\'',end='\'')
print(X,"\'",Y,"\'",Z,"\'")


print(X,Y,Z, sep='\"')
print(X,Y,Z, sep='\"',end='\"')
print(X,"\"",Y,"\"",Z,"\"")

print(X,Y,Z, sep='\\')
print(X,Y,Z, sep='\\',end='\\')
print(X,"\\",Y,"\\",Z,"\\")
