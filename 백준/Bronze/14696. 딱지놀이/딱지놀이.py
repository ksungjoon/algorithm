N = int(input())
lst = [list(map(int,input().split()))for i in range(2*N)]
for i in range(2*N):
    acount = [0, 0, 0, 0, 0]
    bcount = [0, 0, 0, 0, 0]
    if i%2 == 0:
        for t in range(1,5):
            for j in range(1,len(lst[i])):
                if lst[i][j] == t:
                    acount[t] += 1
            for k in range(1,len(lst[i+1])):
                if lst[i+1][k] == t:
                    bcount[t] += 1
        for t in range(4,0,-1):
            if acount[t]>bcount[t]:
                print('A')
                break
            elif acount[t]<bcount[t]:
                print('B')
                break
        if acount==bcount:
            print('D')

