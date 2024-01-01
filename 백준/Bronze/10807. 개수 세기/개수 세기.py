N = input()
lst = list(input().split())
V = input()
cnt = 0
for i in lst:
    if i == V:
        cnt+=1

print(cnt)