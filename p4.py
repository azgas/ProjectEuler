palindromes = []
for i in range(100, 999):
    for j in range(i, 999):
        result = i * j
        result_str = str(result)
        n = len(result_str)
        if result_str[n-n] == result_str[n-1] and result_str[n-n+1] == result_str[n-2]:
            if result_str[n-n+2] == result_str[n-3]:
                palindromes.append(result)

print(palindromes)
print(max(palindromes))

