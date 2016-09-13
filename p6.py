sum_1 = 0
sum_2 = 0
for i in range(1, 101):
    sum_1 = sum_1 + pow(i,2)
for j in range(1,101):
    print(j)
    sum_2 = sum_2 + j


sum_2_2 = pow(sum_2,2)

diff = sum_2_2 - sum_1
print(sum_1)
print(sum_2_2)
print(diff)