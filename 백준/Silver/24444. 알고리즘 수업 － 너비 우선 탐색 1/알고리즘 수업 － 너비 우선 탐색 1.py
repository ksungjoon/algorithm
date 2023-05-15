from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
lst = [[]for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for i in range(M):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()

def bfs (st):
    global cnt
    que = deque()
    que.append(st)
    visited[st] = 1
    while que:
        a = que.popleft()
        for i in lst[a]:
            if visited[i]==0:
                cnt+=1
                visited[i]=cnt
                que.append(i)
bfs(R)
for i in range(1,N+1):
    print(visited[i])


