#11. Create a menu-driven program to perform the following operations: 
# 1 → Addition 
# 2 → Subtraction 
# 3 → Multiplication 
# 4 → Division
print(" 1 → Addition")
print(" 2 → Subtraction")
print(" 3 → Multiplication")
print(" 4 → Division")
print(" 5 → Exit")
ch=int(input("Enter your choice"))
n1=int(input("Enter the Number:"))
n2=int(input("Enter the Number:"))
if(ch==1):
    n3=n1+n2
    print("Result:",n3)
elif(ch==2):
    n3=n1-n2
    print("Result:",n3)
elif(ch==3):
    n3=n1*n2
    print("Result:",n3)
elif(ch==4):
    n3=n1/n2
    print("Result:",n3)
elif(ch==5):
    print("Wrong Choice")
else:
    n3=0
    print("Bye")