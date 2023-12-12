answer = []
def dfs(ban_dict, ban_ids, idx, id_set):
    if len(ban_ids) == idx :
        if set(id_set) not in answer:
            answer.append(set(id_set))
        return

    now = ban_ids[idx]
    for i in range(len(ban_dict[ban_ids[idx]])) :
        if ban_dict[now][i] in id_set :
            continue
        id_set.append(ban_dict[now][i])
        dfs(ban_dict,ban_ids, idx+1, id_set)
        id_set.pop()


def solution(user_id, banned_id):
    banned_dict = {}

    for b in banned_id :
        banned_dict[b] = []

    for bi in banned_id :
        for ui in user_id :
            if len(bi) != len(ui):
                continue
            for idx in range(len(bi)) :
                if bi[idx] == '*':
                    continue
                if bi[idx] != ui[idx] :
                    break
            else :
                if ui not in banned_dict[bi]:
                    banned_dict[bi].append(ui)

    dfs(banned_dict,banned_id,0,[])

    return len(answer)