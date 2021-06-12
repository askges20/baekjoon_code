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

min = int(input())
max = int(input())
sum = 0
minPrime = 0
for j in range(min, max+1):
    if isPrime(int(j)):
        sum += j
        if minPrime == 0:
            minPrime = j
if sum != 0:
    print(sum)
    print(minPrime)
else:
    print(-1)
