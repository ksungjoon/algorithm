N = int(input())
def dfs(case):
    global cnt
    if case <= 0:
        if case == 0:
            cnt+=1
        return
    for i in range(1,4):
        dfs(case-i)

for i in range(N):
    a = int(input())
    cnt = 0
    dfs(a)
    print(cnt)

