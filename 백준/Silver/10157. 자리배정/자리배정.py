C,R = map(int,input().split())
K = int(input())
lst = [[0]*R for i in range(C)]
diry = [0,1,0,-1]
dirx = [1,0,-1,0]
now = 0
dy=0
dx=0
for i in range(1,C*R+1):
    lst[dy][dx]=i
    dx+=dirx[now]
    dy+=diry[now]
    if dx<0 or dy <0 or dx>=R or dy>=C or lst[dy][dx]!=0:
        dy -=diry[now]
        dx -=dirx[now]
        now+=1
        now = now%4
        dy += diry[now]
        dx += dirx[now]
def abc (lst,k):
    for i in range(C):
        for j in range(R):
            if lst[i][j] == k:
                return i+1,j+1
    return [0]

print(*abc(lst,K))