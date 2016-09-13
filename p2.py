sum = 0
i = 1
i_n = 2
while i_n < 4000000:
    print(i_n)
    if i_n % 2 == 0:
        sum = sum + i_n
    ii = i + i_n
    i = i_n
    i_n = ii

print("sum:",sum)