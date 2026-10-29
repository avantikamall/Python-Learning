# 14. Create a menu-driven program to calculate: 
#  1 → Area of Rectangle 
#  2 → Area of Circle 
#  3 → Area of Square 
print(" 1 → Area of Rectangle")
print(" 2 → Area of Circle ")
print(" 3 → Area of Square")
print(" 4 → Exit")
ch=int(input("Enter your choice"))
n1=int(input("Enter the Number:"))
n2=int(input("Enter the Number:"))
if(ch==1):
    n3=n1*n2
    print("Area of Rectangle:",n3)
elif(ch==2):
    n3=2*3.14*n1
    print("Area of Circle:",n3)
elif(ch==3):
    n3=n1**2
    print("Area of Square:",n3)
elif(ch==4):
    print("Wrong Choice")
else:
    n3=0
    print("Bye")