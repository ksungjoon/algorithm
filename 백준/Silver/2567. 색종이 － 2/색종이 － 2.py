N = int(input())
lst = [[0]*102 for i in range(102)]
squre = [list(map(int,input().split()))for _ in range(N)]
length = 0
for i in range(N):
    for j in range(10):
        for k in range(10):
            lst[squre[i][0]+j+1][squre[i][1]+k+1]=1
for i in range(0,101):
    for j in range(0,101):
        if lst[i][j]==0 and lst[i][j+1]==1:
            length+=1
        if lst[i][j]==1 and lst[i][j+1]==0:
            length+=1
        if lst[i][j]==1 and lst[i+1][j]==0:
            length+=1
        if lst[i][j]==0 and lst[i+1][j]==1:
            length+=1
print(length)