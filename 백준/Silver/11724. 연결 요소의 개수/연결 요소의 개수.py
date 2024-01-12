from collections import deque

N,M = map(int,input().split())
lst = list([0]*N for _ in range(N))
for i in range(M):
    a,b = map(int,input().split())
    lst[a - 1][b - 1]=1
    lst[b - 1][a - 1] = 1
cnt = 0
used_n = [0]*N
def bfs(st):
    global used_n
    q = deque()
    q.append(st)
    line = []
    while q:
        now = q.popleft()
        used_n[now] = 1
        line.append(now)
        for i in range(N):
            if lst[now][i] == 1:
                if i not in line and i not in q:
                    q.append(i)
for i in range(len(used_n)):
    if used_n[i] == 0:
        bfs(i)
        cnt+=1
print(cnt)