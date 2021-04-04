import math
num = int(input())
for i in range(num):
    inp = input().split()
    h = int(inp[0])
    w = int(inp[1])
    c = int(inp[2])
    if len(str(math.ceil(c/h))) == 1:
        print(str((c-1)%h+1) + '0' + str(math.ceil(c/h)))
    else:
        print(str((c-1)%h+1) + str(math.ceil(c/h)))
