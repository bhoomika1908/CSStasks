n=int(input("enter a number"))
if n==1 or n==0:
    print("not a prime number")
for i in range(2,n):
    if n%i==0:
        print("is not a prime")
        break
else:
    print("is a prime")