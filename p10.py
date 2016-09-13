from math import sqrt


def silo(n):
    lista = []
    tab = [True]*(n+1)
    lim = int(sqrt(n))
    for i in range(2, lim+1):
        if tab[i]:
            w = i*i
            while w <= n:
                tab[w] = False
                w += i

    for i in range(2, n+1):
        if tab[i]:
            lista.append(i)
    return lista

print(silo(23))
print(sum(silo(2000000)))
