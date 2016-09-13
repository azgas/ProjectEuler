import p3
import collections
# listt = []
# for i in range(1, 11):
#     listt.append(i)

def largest(a, b):
    list1 = p3.primefactors(a)
    list2 = p3.primefactors(b)
    a = collections.Counter(list1)
    b = collections.Counter(list2)
    a_keys = list(a.keys())
    a_val = list(a.values())
    b_keys = list(b.keys())
    b_val = list(b.values())
    keys = a_keys + b_keys
    keys = set(keys)
    nww = 1
    for k in keys:
        if k in a_keys:
            ia = a_keys.index(k)
            av = a_val[ia]
        else:
            av = 1
        if k in b_keys:
            ib = b_keys.index(k)
            bv = b_val[ib]
        else:
            bv = 1

        number = max(av, bv)
        nww *= pow(k,number)
    return nww
n = 1
for i in range(2, 21):
    n = largest(n, i)

print(n)