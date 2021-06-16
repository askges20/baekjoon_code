n=int(input())
stair=[]
for i in range(n):
    stair.append(int(input()))

score=[stair[0]] #score[k]:k+1번째 계단까지 최대 점수
if n>=2:
    score.append(stair[0]+stair[1])
if n>=3:
    score.append(max(stair[0],stair[1])+stair[2])
for j in range(3,n):
    score.append(max(score[j-2]+stair[j], score[j-3]+stair[j-1]+stair[j]))
    #k번째 계단 최대 점수 : (k-2번째 계단까지 최대 + k번째 계단 점수) or (k-3번째 계단까지 최대 + k-1번째 계단 점수 + k번째 계단 점수)
print(score[n-1])
