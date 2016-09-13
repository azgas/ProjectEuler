t = True
while t:
    for a in range(1,999):
        for b in range(a,1000):
            c = 1000 - a - b
            if pow(c, 2) == pow(a, 2) + pow(b, 2):
                t = False
                print(a, b, c)
                print(a*b*c)