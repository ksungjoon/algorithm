from copy import deepcopy
from collections import deque

def bfs(arr,x,y):
    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        y.append(now)
        for i in range(x):
            if arr[now][i]==1:
                if i not in y and i not in q:
                    q.append(i)
    return y

def solution(n, wires):
    answer = 21e9
    for i in range(len(wires)):
        lst= deepcopy(wires)
        lst.pop(i)
        check = [[0]*n for _ in range(n)]
        for i in range(len(lst)):
            check[lst[i][0]-1][lst[i][1]-1] = 1
            check[lst[i][1]-1][lst[i][0]-1] = 1
        a = []
        result = bfs(check,n,a)
        if answer> abs(n-2*len(result)):
            answer = abs(n-2*len(result))
    return answer