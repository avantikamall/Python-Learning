#  Take two numbers and print all numbers that are even and divisible by 6. 
n=int(input("Enter a Number:"))
m=int(input("Enter a Number:"))
div=0
for i in range(n,m+1,1):
    if(i%6==0 and i%2==0):
        print(i)