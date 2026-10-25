import numpy as np
marks=np.array([67,87,46,93,37])
mask =marks>=50
print(mask)
print(marks[mask])
result = np.where(marks>50,"Pass","Fail")
print(result)

#practical
marks=np.array([35, 82, 49, 91, 50, 67])
mask=marks>=50
print(marks[mask])
result=np.where(marks>=50,"Pass","Fail")
print(result)