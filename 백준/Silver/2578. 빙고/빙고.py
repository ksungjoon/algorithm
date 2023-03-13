lst = [list(map(int,input().split()))for i in range(5)] # 빙고판 입력받음
call_lst = [list(map(int,input().split()))for j in range(5)] # 부르는 숫자 입력받음
cnt = 0  # 숫자 지울때 마다 카운트 되는 변수 생성

def xyresult():
    global resultcnt
    for i in range(5):
        ysum = 0
        if sum(lst[i])==0:
            resultcnt +=1
        for j in range(5):
            ysum+=lst[j][i]
        if ysum == 0:
            resultcnt +=1
def cross ():
    global resultcnt
    lcross = 0
    rcross = 0
    for i in range(5):
        lcross+=lst[i][i]
        rcross+=lst[i][-(i+1)]
    if lcross ==0:
        resultcnt+=1
    if rcross == 0:
        resultcnt+=1

def map(x):
    for i in range(5):
        for j in range(5):
            if lst[i][j]==x:
                lst[i][j]=0

for i in range(5):
    for j in range(5):
        resultcnt = 0
        map(call_lst[i][j])
        cnt+=1
        cross()
        xyresult()
        if resultcnt >= 3:
            break
    if resultcnt>=3:
        break
print(cnt)