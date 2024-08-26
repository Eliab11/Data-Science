import numpy as np

my_1d_array = np.zeros(10)
print(my_1d_array)

my_1d_array[0] = 50

print(my_1d_array)


my_1d_array[3:6] = 50

print(my_1d_array)

np.where(my_1d_array  == 50)


my_2d_array = np.array([[1,5,9],[8,5,5]])
print(my_2d_array)

np.where(my_2d_array == 5)
np.where(my_2d_array < 5)
np.where(my_2d_array > 5)

np.where(my_2d_array == 5)