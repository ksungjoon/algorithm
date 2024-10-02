def solution(name):
    count = 0
    N = len(name)

    for ch in name: # 2. 먼저 커서가 어디있든, A에서 최소로 바꿔야 그 글자가 되는지 모두 계산한다
        if (ch != 'A'):
            min_up_down = min(ord(ch) - ord('A'), 26 + ord('A') - ord(ch))
            count += min_up_down
    
    move = N - 1 # 1. 커서를 좌우로 움직이는 것은, 아무리 최악이어도 문자열을 한번 순회하는 것뿐이다 -> N - 1
    for left in range(N):
        idx = left + 1
        while (idx < N) and (name[idx] == 'A'): # right는 오른쪽 끝에서, left 오른쪽을 기준으로 처음 A가 아닌 알파벳의 위치만큼 빼줘야 한다!
            idx += 1
            
        right = N - idx
        back_distance = min(left, right) # 한쪽 방향으로 이동 후, 반대 방향으로 이동하는 최소거리를 구한다 -> 그러므로 left나 right 중 최솟값을 한번 더 더하는 것이다.
        
        move = min(move, left + right + back_distance)
    
    count += move
    return count