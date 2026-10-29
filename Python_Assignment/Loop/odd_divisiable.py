#  Take two numbers and print all numbers that are odd and divisible by 3.
n=int(input("Enter a Number:"))
m=int(input("Enter a Number:"))
div=0
for i in range(n,m+1,1):
    if(i%3==0 and i%2!=0):
        print(i)