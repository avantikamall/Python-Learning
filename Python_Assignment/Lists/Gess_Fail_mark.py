# 9.  Count how many students failed, assuming passing marks are 40. 
marks = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
count=0
for i in range(0,len(marks),1):
    if(marks[i]<=40):
       count=count+1
print(count)