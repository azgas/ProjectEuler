from p3 import primefactors
def findnumberoffactors(x):
    primes = primefactors(x)
    howmanytimes = {p:primes.count(p) for p in primes}
    result = 1
    for i in howmanytimes.values():
        result *= (i+1)

    return result

# def trianglenumber(x):
#     if x == 1:
#         result = 1
#     else:
#         result = trianglenumber(x-1) + x
#     return result

# x = 100
# while findnumberoffactors(trianglenumber(x)) < 500:
#     x += 1
x = 28
i = 8
while findnumberoffactors(x)<500:
    x += i
    i += 1

print(x)
# print(trianglenumber(x))