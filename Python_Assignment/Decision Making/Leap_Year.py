#  Check whether a given year is a leap year. 
Year=int(input("Enter the year to know the Leap year or not:"))
if(Year%4==0 and Year%400==0):
    {
        print("Its a Leap Year")
    }
else:
    print("Not a Leap Year")