import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = [input().rstrip() for _ in range(N)]
see = [input().rstrip() for _ in range(M)]

ans = list(set(listen) & set(see))

ans.sort()
print(len(ans))
for a in ans:
    print(a)