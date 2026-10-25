import numpy as np

marks_arr = np.array([70, 85, 90, 60, 95])

print(marks_arr.sum())
print(marks_arr.mean())
print(marks_arr.max())
print(marks_arr.min())

#axis
scores_arr = np.array([[70, 80, 90],
                       [60, 75, 95]])

print(scores_arr.sum(axis=0))
print(scores_arr.sum(axis=1))
print(scores_arr.mean(axis=1))

#argmax & argmin
print(marks_arr.argmax())   #index of max value
print(marks_arr.argmin())


#practical
study_arr=np.array([[2, 3, 1, 4, 3, 2],[3, 3, 2, 5, 4, 1]])
print(study_arr.sum(axis=1))
print(study_arr.mean(axis=0))
print(study_arr[1,].argmax())
print(study_arr.max())
