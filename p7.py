def main():
    lp = 0
    k = 1
    d = 1
    p = 2
    tlp = []
    while lp<10001:
        t = True
        if lp<3:
            p += lp
        else:
            p = 6*k + d
            if d == 1:
                d = -1
                k += 1
            else:
                d = 1
            g = int(round(p))
            i = 2
            while tlp[i] <= g:
                if p % tlp[i] == 0:
                    t = False
                    break
                if i<len(tlp)-1:
                    i += 1
                else:
                    break
        if t:
            tlp.append(p)
            lp += 1
    print(tlp[lp-1])
main()


