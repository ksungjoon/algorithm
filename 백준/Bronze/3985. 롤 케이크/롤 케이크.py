L= int(input())
N = int(input())
lst = [list(map(int,input().split()))for i in range(N)]
bread = [0]*(L+1)
exmax = -21e9
exnum = 0
realmax= -21e9
realnum= 0
for i in range(N):
    if exmax< lst[i][1]-lst[i][0]:
        exmax=lst[i][1]-lst[i][0]
        exnum=i+1
for i in range(N):
    for j in range(lst[i][0],lst[i][1]+1):
        if bread[j]!=0:
            continue
        bread[j]=i+1
for i in range(1,N+1):
    cnt = 0
    for j in bread:
        if i == j:
            cnt +=1
    if realmax<cnt:
        realmax =cnt
        realnum = i
print(exnum)
print(realnum)