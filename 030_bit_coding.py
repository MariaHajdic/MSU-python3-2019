def shex(n):
    res = []
    while n:
        res.append(chr(32 + (n & 63)))
        n >>= 6
    return "".join(res[::-1])

def xehs(s):
    val = 0
    for c in s:
        val <<= 6
        val += ord(c) - 32
    return val

def encode(txt):
    dic = {}
    for i in txt:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    keys = list(dic.keys())
    keys.sort(key=lambda x: (dic[x], x), reverse=True)

    bits_dic = {}
    begin = 0
    for i, val in enumerate(keys):
        v = begin
        begin += 1 << (i + 1)
        bits_dic[val] = (v, i + 1)

    flen = 0
    res = 0
    acc = []
    for s in txt:
        flen += bits_dic[s][1]
        res <<= bits_dic[s][1]
        res += bits_dic[s][0]
        while flen >= 6:
            acc.append(chr(32 + ((res >> (flen - 6)) & 63)))
            flen -= 6
        res &= 63

    if flen != 0:
        k = (res << (6 - flen)) & 63
        acc.append(chr(32 + k))

    while res % 64:
        res <<= 1

    return (len(txt), "".join(keys), "".join(acc))

def decode(ln, tops, cypher):
    dic = {}
    begin = 1
    for k in tops:
        dic[begin] = k
        begin *= 2

    res = []
    char = 1
    dec = xehs(cypher)
    while dec:
        if dec & 1:
            char *= 2
        else:
            res.append(dic[char])
            char = 1
        dec >>= 1

    res.append(dic[char])
    return "".join(res[::-1])[:ln]
