N,X = map(int,input().split())
lst = list(map(int,input().split()))
answer = []
for i in lst:
    if i<X:
        answer.append(i)
print(*answer)