T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    lst=[list(input())for i in range(N)]
    min = 21e9
    count_lst=[]
    for i in range(N):
        w=M-lst[i].count('W')
        b=M-lst[i].count('B')
        r=M-lst[i].count('R')
        count_lst.append([w,b,r])
    for w in range(N-2):
        for b in range(1,N-w-1):
            r= N-w-b-2
            result = 0
            for i in range(w):
                result+=count_lst[i+1][0]
            for j in range(w,b+w):
                result+=count_lst[j+1][1]
            for k in range(b+w,r+w+b):
                result+=count_lst[k+1][2]
            result+= count_lst[0][0]+count_lst[N-1][2]
            if result<min:
                min = result
    print(f'#{test_case} {min}')
