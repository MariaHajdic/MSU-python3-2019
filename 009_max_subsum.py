import sys

def maxSubArraySum(a,size):    
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 

numbers = []
while (True):
    n = int(input())
    if (n == 0): break
    numbers.append(n)

print(maxSubArraySum(numbers,len(numbers)))
