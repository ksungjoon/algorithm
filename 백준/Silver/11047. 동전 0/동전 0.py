N,K = map(int,input().split())
lst = list(int(input())for _ in range(N))
mok = 0

for i in range(len(lst)-1,-1,-1):
    if K//lst[i]>=1:
        mok+=K//lst[i]
        K = K%lst[i]
    if K == 0:
        break
print(mok)