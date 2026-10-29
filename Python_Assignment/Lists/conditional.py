# 13. Create a list of marks and count how many students scored between 40 and 60. 
marks = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
count=0
for i in range(0,len(marks),1):
    if(marks[i]>=40 and marks[i]<=60):
       count=count+1
print(count)