# print(2**3)

def rtp(base, pow):
    res = 1
    for idx in range(pow):
        res = res * base
    return res


print(rtp(2, 3))