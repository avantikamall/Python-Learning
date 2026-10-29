# 18. Given a list of student marks, create two lists:
#●  pass_students 
#●  fail_students
marks = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
pass_students=[]
fail_students=[]
for i in range(0,len(marks),1):
    if(marks[i]>=40):
        pass_students.append(marks[i])
    else:
        fail_students.append(marks[i])
print("Pass students:", pass_students)
print("Fail students",fail_students)