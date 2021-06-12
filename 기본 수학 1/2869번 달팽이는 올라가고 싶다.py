import math
inp = input().split()
a = int(inp[0])
b = int(inp[1])
v = int(inp[2])
print(math.ceil((v-a)/(a-b))+1)
