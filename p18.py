import numpy as np

txtfile = open('p18.txt')
count_line = sum(1 for line in txtfile)
matrix = np.zeros((count_line, count_line))

txtfile = open('p18.txt')
i = 0
for line in txtfile: # filling matrix with data
    arr = line.split()
    for j in range(0, len(arr)):
        matrix[i, j] = arr[j]
    i += 1

start_line = count_line - 2
for current in range(start_line, -1, -1):
    for j in range(0, current + 1):
        matrix[current, j] += max(matrix[current + 1, j], matrix[current + 1, j + 1])

print(matrix[0, 0])