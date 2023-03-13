N = int(input())
lstnum = list(map(int,input().split())) 
student = [i for i in range(1,N+1)] 
result = [] 
for i in range(N):
    result.insert(i-lstnum[i],student[i])
print(*result)