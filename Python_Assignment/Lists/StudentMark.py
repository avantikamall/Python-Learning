# 12. Create a list of student marks 
# and count how many students scored above 80.
Marks=[23,33,44,55,66,77,88,99,100]
count=0
for i in range(0, len(Marks), 1):
     if(Marks[i]<=80):
           count=count+1
print(count)