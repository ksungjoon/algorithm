H,K = map(int,input().split())
lst = [list(input())for i in range(H)]
for i in range(H):
    for j in range(K):
        if lst[i][j]=='.':
            lst[i][j]=-1
        if lst[i][j]=='c':
            lst[i][j]=0
for i in range(H):
    for j in range(1,K):
        if lst[i][j-1]!= -1 and lst[i][j]!= 0:
            lst[i][j]=lst[i][j-1]+1
for i in range(H):
    print(*lst[i])
