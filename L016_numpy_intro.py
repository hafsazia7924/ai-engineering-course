import numpy as np

marks_list = [10, 20, 30]
marks = np.array(marks_list)

print(marks_list)
print(marks)
print(type(marks))

print(marks_list * 2)
print(marks * 2)
print(marks + 5)

print(marks.shape)
print(marks.dtype)

prices = np.array([1.5, 2, 3])
print(prices)
print(prices.dtype)


#practical
temp_in_c=[30, 35, 40, 28, 32]
temp=np.array(temp_in_c)
temp_in_f=temp* 9 / 5 + 32
print(temp_in_f)
print(temp_in_f.shape)
print(temp_in_f.dtype)