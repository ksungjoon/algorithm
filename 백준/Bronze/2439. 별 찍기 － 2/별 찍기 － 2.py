N = int(input())
star = [' ']*N
for i in range(1,N+1):
    star[-i]='*'
    print(*star,sep='')