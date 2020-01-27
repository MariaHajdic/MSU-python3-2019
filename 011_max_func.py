def maxfun(n, *args):
    sum_max = sum(map(args[0], n))
    res = 0
    for _, val in enumerate(args):
        sum_tmp = sum(map(val, n))
        if sum_tmp >= sum_max:
            sum_max = sum_tmp
            res = val
    return res
