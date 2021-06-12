import math

def isPrime(num):
    cnt = 0
    if num == 1:
        return False
    for k in range(1, num+1):
        if num % k == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

inp = input().split()
min = int(inp[0])
max = int(inp[1])

nums = []
for i in range(0, max+1):
    nums.append('-')

#에라토스테네스의 체 이용
for j in range(1, int(math.sqrt(max))+1):
    if nums[j] == '-':
        if isPrime(j):
            nums[j] = 'o'
            for k in range(j, len(nums), j):
                if nums[k] == '-':
                    nums[k] = 'x'
        else:
            nums[j] = 'x'
for a in range(min, len(nums)):
    if nums[a] != 'x':
        print(a)
