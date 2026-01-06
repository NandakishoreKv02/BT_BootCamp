n=int(input("Enter a number: "))
start=5
a=1
b=1
for i in range(1,n+1):
    print(start,end=" ")
    start+=a
    a,b=b,a+b

