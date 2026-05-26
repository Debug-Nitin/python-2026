import math
n = int(input())
temp = n
sum_fact = 0
while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)
    temp //= 10
print('Yes' if sum_fact == n else 'No')