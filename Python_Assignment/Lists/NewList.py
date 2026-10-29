# 17. Given a list of numbers, create a new list containing only even numbers. 
marks = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
Marks_Even=[]
for i in range(0,len(marks),1):
    if(marks[i]%2==0):
        Marks_Even.append(marks[i])
print("Even:",Marks_Even)