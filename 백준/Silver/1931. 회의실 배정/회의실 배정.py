N = int(input())
lst = [list(map(int,input().split()))for i in range(N)]
lst = sorted(lst,key=lambda x:(x[1],x[0]))

time = 0
answer = 0
for i in range(N):
    if time <= lst[i][0]:
        time = lst[i][1]
        answer+=1
print(answer)