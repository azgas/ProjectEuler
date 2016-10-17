def chain(x):
    lista = []
    lista.append(x)
    while x > 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
        lista.append(x)
    return lista


def len_of_chain(x):
    leng = 0
    while x > 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
        leng += 1
    return leng

max = 0
x = 0
scope = list(range(1, 1000000))
# nieefektywne
# for i in scope[:]:
#     chain_temp = chain(i)
#     if len(chain_temp) > max:
#         max = len(chain_temp)
#         x = i
#     for num in chain_temp:
#         if num in scope:
#             scope.remove(num)


    # i += 1
    # chain_temp = chain(scope[i])
    # results.append(len(chain_temp))
    # for number in chain_temp:
    #     if any(num == number for num in scope):
    #         scope.remove(number)


for i in scope[:]:
    i_length = len_of_chain(i)
    if i_length > max:
        max = i_length
        start = i

print(max, " ", start)



