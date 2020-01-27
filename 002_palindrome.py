num = int(input())
rev = 0
temp = num

while (temp > 0):
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10

if (num == rev):
    print("YES")
else:
    print("NO")
