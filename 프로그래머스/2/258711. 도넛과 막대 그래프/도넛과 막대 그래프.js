// javascript

function solution(edges) {
    // 최대 노드 번호 찾기
    let max_val = 0;
    for (const [now_out, now_in] of edges) {
        max_val = Math.max(max_val, now_out, now_in);
    }
    max_val += 1;  
    // 배열 크기 조정을 위해 +1

    let answer = [0, 0, 0, 0]; // 생성 정점, 도넛, 막대, 8자
    let in_cnt = Array(max_val).fill(0);
    let out_cnt = Array(max_val).fill(0);

    // in, out 간선 갯수 저장
    edges.forEach(([now_out, now_in]) => {
        if (now_out < max_val && now_in < max_val) {
            out_cnt[now_out]++;
            in_cnt[now_in]++;
        }
    });

    // 유형별 판별
    for (let now_node = 1; now_node < max_val; now_node++) {
        if (in_cnt[now_node] === 0 && out_cnt[now_node] >= 2) { // 생성 노드
            answer[0] = now_node;
        } else if (in_cnt[now_node] >= 1 && out_cnt[now_node] === 0) { // 막대 그래프
            answer[2]++;
        } else if (in_cnt[now_node] >= 2 && out_cnt[now_node] === 2) { // 8자 그래프
            answer[3]++;
        }
    }

    // 도넛 그래프 계산
    answer[1] = out_cnt[answer[0]] - answer[2] - answer[3]

    return answer;
}
