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

inps = []
while True:
    inp = int(input())
    if inp == 0:
        break
    inps.append(inp)

#에라토스테네스의 체 이용
for n in inps:
    nums = []
    for i in range(0, 2*n+1):
        nums.append('-')

    for j in range(1, int(math.sqrt(2*n))+1):
        if nums[j] == '-':
            if isPrime(j):
                nums[j] = 'o'
                for k in range(j, len(nums), j):
                    if nums[k] == '-':
                        nums[k] = 'x'
            else:
                nums[j] = 'x'
    print(nums[n+1:2*n+1].count('o')+nums[n+1:2*n+1].count('-'))
