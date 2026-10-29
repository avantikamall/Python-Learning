# Find the factorial of a given number. 
n=int(input("Find the Factorial for a number:"))
f=1
e=""
for i in range(n,0,-1):
    f=f*i
    if i==1:
        e=e+str(i)
    else:
        e=e+str(i)+"x"
print(e,"=",f)