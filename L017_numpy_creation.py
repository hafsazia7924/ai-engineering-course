import numpy as np

zeros_arr = np.zeros(5)
ones_arr = np.ones((2, 3))

print(zeros_arr)
print(ones_arr)
print(ones_arr.shape)
print(zeros_arr.dtype)

steps_arr = np.arange(0, 10, 2)         #start,stop,count
points_arr = np.linspace(0, 1, 5)

print(steps_arr)
print(points_arr)


flat_arr = np.arange(12)
grid_arr = flat_arr.reshape(3, 4)
auto_arr = flat_arr.reshape(2, -1)

print(flat_arr)
print(grid_arr)
print(auto_arr)
print(grid_arr.shape)
print(auto_arr.shape)

random_num=np.random.default_rng(42)    #rng->random number generator
array=random_num.random(5)
random_num1=np.random.default_rng(42)    #for same random nums as above
array2=random_num1.random(5)
print(array)
print(array2)
print(array==array2)

#practical
days_arr=np.arange(1,13,1)
new_arr=days_arr.reshape(3,-1)
marks=np.linspace(40,100,5)
zeros=np.zeros((2,3))
print(days_arr)
print(new_arr)
print(new_arr.shape)
print(marks)
print(zeros)