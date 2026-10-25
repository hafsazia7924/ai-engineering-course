import numpy as np

marks = np.array([10, 20, 30, 40, 50])

#indexing
print(marks[0])
print(marks[3])
print(marks[-1])
print(marks[-2])

#slicing
print(marks[1:4])
print(marks[0:2])
print(marks[2:5])

#shortcut code
print(marks[:3])       #all before 3rd index
print(marks[2:])       #all ater 2nd index
print(marks[-2:])      #all after 2nd last index

#2D arrays
class_marks = np.array([[10, 20, 30],
                        [40, 50, 60],
                        [70, 80, 90]])
#for indexing
print(class_marks[0, 0])
print(class_marks[1, 2])
print(class_marks[2, 1])
#full row or column
print(class_marks[0])     #0th row
print(class_marks[1, :])   #1st row
print(class_marks[:, 1])  #first colum
#for slicing
print(class_marks[0:2, 1:3])
print(class_marks[1:, :2])
print(class_marks[1:, 1:])

#values changing
marks[0] = 15
print(marks)

marks[3:] = 99   #after 3rd index all marks change
print(marks)

class_marks[0, 0] = 0
print(class_marks)

#skipping items
digits = np.arange(10)

print(digits)
print(digits[::2])         #start:stop:step
print(digits[1:8:3])
print(digits[::-1])


#view vs copy
original = np.array([1, 2, 3, 4, 5])

part = original[1:4]
part[0] = 99
print(original)
print(part)

safe_part = original[1:4].copy()
safe_part[0] = 0
print(original)
print(safe_part)

#practical
score_arr=np.array([45, 60, 72, 88, 91, 55, 67, 80])
print(score_arr[:3])
print(score_arr[-2:])
print(score_arr[::2])
print(score_arr[::-1])
last_three_copy=score_arr[-3:].copy()
last_three_copy[0]=0
print(score_arr)
print(last_three_copy)

grid_arr=np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
print(grid_arr[1,])
print(grid_arr[:,1])
print(grid_arr[:2,:2])
