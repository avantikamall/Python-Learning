#  Take a number from the user and print its multiplication table.
j=int(input("Enter a Number:"))
for i in range(1,11,1):
     print(f"{j} x {i} = {j * i}")
