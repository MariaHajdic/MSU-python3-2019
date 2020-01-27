k = int(input())
res, additional = 0, 0
digit = k
i = 1

while True:
    res += digit * i
    val = digit * k + additional
    digit = val % 10
    additional = val // 10
    if digit == k and additional == 0:
        break
    i *= 10

print(res)
