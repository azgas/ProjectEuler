file = open('grid_for_p11.txt')
a = []
i = 0
for line in file:
    a.append(line)
    i += 1


product_list = []
for i in range(0, len(a)):
    a[i] = a[i][:-1]
    a[i] = a[i].split()
    for j in range(0, len(a[i])):
        a[i][j] = int(a[i][j])

#po wierszach
max_prod = 1
for i in range(0, len(a)):
    for j in range(0, len(a[i])-3):
        max_prod_n = 1
        for k in range(j, j+4):
            max_prod_n *= a[i][k]
        if max_prod_n > max_prod:
            max_prod = max_prod_n


product_list.append(max_prod)

#po kolumnach
max_prod = 1
for i in range(0, len(a)):
    for j in range(0, len(a[i])-3):
        max_prod_n = 1
        for k in range(j, j+4):
            max_prod_n *= a[k][i]
        if max_prod_n > max_prod:
            max_prod = max_prod_n

product_list.append(max_prod)

#diagonalnie od lewej do prawej(w dół) - połówka góra-prawo
max_prod = 1
for i in range(0, len(a)):
    for j in range(0, len(a[i])-3-i):
        max_prod_n = 1
        for k in range(j, j+4):
            max_prod_n *= (a[k][k+i])
        if max_prod_n > max_prod:
            max_prod = max_prod_n

product_list.append(max_prod)

#diagonalnie od lewej do prawej - połówka lewy-dół
max_prod = 1
for i in range(0, len(a)):
    for j in range(0, len(a[i])-3-i):
        max_prod_n = 1
        for k in range(j, j+4):
            max_prod_n *= (a[k+i][k])
        if max_prod_n > max_prod:
            max_prod = max_prod_n

product_list.append(max_prod)


#diagonalnie od prawej do lewej(w dół), iterowanie po wierszach
max_prod = 1
for i in range(0, len(a)):
    for j in range(0, len(a[i])-3-i):
        max_prod_n = 1
        for k in range(j, j+4):
            max_prod_n *= (a[len(a)-(k+i)-1][k])
        if max_prod_n > max_prod:
            max_prod = max_prod_n

product_list.append(max_prod)

#j.w. iterowanie po kolumnach
max_prod = 1
for i in range(0, len(a)):
    for j in range(0, len(a[i])-3-i):
        max_prod_n = 1
        for k in range(j, j+4):
            max_prod_n *= (a[k][len(a) - k - 1])
        if max_prod_n > max_prod:
            max_prod = max_prod_n

product_list.append(max_prod)
print(product_list)
print(max(product_list))