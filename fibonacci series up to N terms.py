#fibonacci series up to N terms:
n=int(input("Enter N:"))
a= 0#previous term
b=1 #current term
for i in range(n):
    print(a)
    nxt=a+b #next term 
    a=b
    b=nxt 