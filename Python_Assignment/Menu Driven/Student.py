#12. Create a menu-driven program for a student: 
# 1 → Display Student Name 
#  2 → Display Student Marks 
# 3 → Display Student Grade
print("1 → Display Student Name ")
print("2 → Display Student Marks")
print("3 → Display Student Grade")
ch=int(input("Enter Your Choice :"))
Name=input("Enter Your Name :")
Marks=float(input("Enter Your Marks :"))
if(ch==1):
    print(f"Your Name is :{Name}")
elif(ch==2):
    print(f"Your marks are :{Marks}")
elif(ch==3):
    if(Marks>=80 and Marks<=100):
        print(f"Your Name:{Name},and Mark:{Marks},So the Grade is A")
    elif(Marks>=60 and Marks<=79):
        print(f"Your Name:{Name},and Mark:{Marks},So the Grade is B")
    elif(Marks>=40 and Marks<=5):
        print(f"Your Name:{Name},and Mark:{Marks},So the Grade is C")
    else:
        print("Fail")
else:
    print(f"Wrong Choise")