N,K = map(int,input().split())
lst = [list(map(int,input().split()))for i in range(N)]
count = 0
man_class = [0,0,0,0,0,0]
woman_class = [0,0,0,0,0,0]
for i in range(N):
    if lst[i][0] ==0:
        woman_class[lst[i][1]-1]+=1
    else:
        man_class[lst[i][1]-1]+=1
for i in range(6):
    count += man_class[i]//K
    if man_class[i]%K !=0:
        count+=1
    count += woman_class[i]//K
    if woman_class[i]%K !=0:
        count+=1
print(count)