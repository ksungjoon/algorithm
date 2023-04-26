from collections import deque
N = int(input())
M = int(input())
arr=[[0]*(N+1)for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1
cnt = 0
used = [0]*(N+1)
def bfs(st):
    global cnt
    que = deque()
    que.append(st)
    while que:
        now = que.popleft()
        cnt+=1
        for i in range(N+1):
            if arr[now][i]==1 and used[i] != 1:
                used[i]=1
                que.append(i)

used[1]=1
bfs(1)
print(cnt-1)
