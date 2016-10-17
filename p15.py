import queue
import time
# nieefektywne
def FindPaths(size):
    paths = 1
    q = queue.Queue()
    q.put([0, 0])
    while not q.empty():
        flag_1 = False
        flag_2 = False
        current = q.get()
        if current[0]+1 <= size:
            flag_1 = True
            q.put([current[0] + 1, current[1]])
        if current[1]+1 <= size:
            flag_2 = True
            q.put([current[0], current[1] + 1])
        if flag_1 and flag_2:
            paths += 1
    print(paths)


# start = time.time()
# FindPaths(3)
# time = time.time() - start
# print(time)

def FindPahtsMatrix(dim1, dim2):
    matrix = [[0 for j in range(dim2 + 1)] for i in range(dim1 + 1)]
    for i in range(dim1+1):
        for j in range(dim2+1):
            if i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    print(matrix[dim1][dim2])

start_time = time.time()
FindPahtsMatrix(20, 20)
end_time = time.time() - start_time
print("time: " + str(end_time))
