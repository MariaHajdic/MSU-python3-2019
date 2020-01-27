import math

def is_power(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if i ** int(math.log(num, i)) == num:
            return True
    return False
    
num = int(input())

if (num == 0):
    print("NO")
elif (num == 1):
    print("YES")
else:
    if (is_power(num)):
        print("YES")
    else:
        print("NO")
