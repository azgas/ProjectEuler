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

print(chain(13))
