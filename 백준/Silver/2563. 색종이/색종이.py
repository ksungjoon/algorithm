N = int(input())
paper = [ list(map(int,input().split())) for i in range(N)]
white = [[0]*101 for i in range(101)] # 100 행 100 열

for i in range(len(paper)):
    x_start=paper[i][0]
    x_end=paper[i][0]+10
    y_start=paper[i][1]
    y_end=paper[i][1]+10

    for x in range(x_start,x_end):
        for y in range(y_start,y_end):
            white[x][y] = 1

result = 0
for x in range(0,100):
    for y in range(0,100):
        result += white[x][y]

print(result)