# 16. Given a list of numbers, create a new list containing numbers greater than 50. 
marks = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
Mark_Copy=[]
for i in range(0,len(marks),1):
    if(marks[i]>50):
        Mark_Copy.append(marks[i])
print(Mark_Copy)
Mark_Copy.sort(reverse=True)
print(Mark_Copy)