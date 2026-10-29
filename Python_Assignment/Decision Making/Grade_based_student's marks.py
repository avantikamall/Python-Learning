# 8.  Display a grade based on the student's marks: 
#80–100 → A 
#60–79 → B 
#40–59 → C 
#Below 40 → Fail
Marks=float(input("ENter Your Marks :"))
if(Marks>=80 and Marks<=100):
    {
        print("Your Grade is A",Marks)
    }
elif(Marks>=60 and Marks<=79):
    {
        print("Your Grade is B",Marks)
    }
elif(Marks>=40 and Marks<=5):
    {
        print("Your Grade is C",Marks)
    }
else:
    print("Fail")