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

n = int(input())
cnt = 0
nums = input().split()
for j in nums:
    if isPrime(int(j)):
        cnt += 1
print(cnt)
