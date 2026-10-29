# 15. Given a list of numbers, count how many numbers are even and odd.
Num = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
counte=0
counto=0
for i in range(0,len(Num),1):
    if(Num[i]%2==0):
        counte+=1
    else:
        counto+=1
print(f"Your Even number are :{counte}")
print(f"Your Odd number are : {counto}")