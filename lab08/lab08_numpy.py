import numpy as np
# task 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6)
unknown_table = np.ones((2, 3)) * -1
identity = np.eye(3)
print(hours, hours.shape, hours.ndim, hours.size, hours.dtype, sep='\n')
print()
# task 2
print(hours[2], hours[-1], hours[2:6], hours[1::2], hours[::-1], sep='\n')
print()
# task 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape, temperatures.ndim, temperatures.size, sep='\n')
print(temperatures[1, 2], temperatures[0], temperatures[:, 2], temperatures[:2, 1:], sep='\n')
print(temperatures[0:2, 1:3])
print()
# task 4
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[:3], matrix[:3].shape)
print(matrix[-2:], matrix[-2:].shape)
print(matrix[:, :2], matrix[:, :2].shape)
print(matrix[1:4, 2:5], matrix[1:4, 2:5].shape)
print(matrix[-2:, -2:], matrix[-2:, -2:].shape)
print()
# task 5
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print(changed_hours, hours, sep='\n')
# copy нужна чтобы не изменять оригинальный объект
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix, matrix, sep='\n')
