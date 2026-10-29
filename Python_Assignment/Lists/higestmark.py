# 14. Given a list of marks, find the second-highest mark.
marks = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
marks.sort(reverse=True)
print(marks[1])