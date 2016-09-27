file = open('for_p13.txt')
result = 0
for line in file:
    result += int(line)

print(str(result)[0:10])
