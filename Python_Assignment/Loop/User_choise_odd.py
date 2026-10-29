#  Take two numbers from the user and print all odd numbers between them. 
i=int(input("Enter a Number :"))
j=int(input("Enter a Number :"))
for i in range(i,j+1,1):
     if(i%2!=0):
            print(i)