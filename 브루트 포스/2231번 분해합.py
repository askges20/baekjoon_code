n = int(input())
for i in range(1, n+1):
    each = []
    tmp = i
    while True:
        if tmp >= 10:
            each.append(tmp%10)
            tmp = tmp//10
        else:
            each.append(tmp)
            break
    if i+sum(each) == n:
        print(i)
        break
if i == n:
    print(0)
