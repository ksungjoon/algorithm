N,L = map(int,input().split())
lst = [list(map(int,input().split()))for i in range(N)]
load = [[0]for i in range(L)]
time = -1
for i in range(N):
    load[lst[i][0]-1]=[lst[i][1],lst[i][2]]
for i in range(L):
    time+=1
    if load[i]!=[0]:
        for k in range(load[i][0]+load[i][1]):
            if time%(load[i][0]+load[i][1])>=load[i][0]:
                break
            elif time%(load[i][0]+load[i][1])<=load[i][0]:
                time+=1
print(time)