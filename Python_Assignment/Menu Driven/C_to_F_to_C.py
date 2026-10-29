# 15. Create a menu-driven program to convert: 
#  1 → Celsius to Fahrenheit 
#  2 → Fahrenheit to Celsius
print("1 → Celsius to Fahrenheit ") 
print("2 → Fahrenheit to Celsius")
ch=int(input("Enter Your Choise:"))
#n2=input("Inter in the Celcicus :")
if(ch==1):
    C=float(input("Enter in the Celcicus :"))
    D=C*1.8
    F=D+32
    print("Celsius to Fahrenheit",F)
elif (ch==2):
    E=float(input("Enter in the Fahrenheit :"))
    G=E-32
    J=G/1.8
    print("Fahrenheit to Celsius :",J)
else:
    print("Exit")
