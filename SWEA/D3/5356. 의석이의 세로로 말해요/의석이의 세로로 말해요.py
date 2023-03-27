T = int(input())
for test_case in range(1,T+1):
    lst = [input()for i in range(5)]
    a= max(len(lst[i])for i in range(5))
    arr = [['']*a for i in range(5)]
    word = ''
    for i in range(5):
        for j in range(len(lst[i])):
            arr[i][j]=lst[i][j]
    for i in range(a):
        for j in range(5):
            word += arr[j][i]
    print(f'#{test_case} {word}')