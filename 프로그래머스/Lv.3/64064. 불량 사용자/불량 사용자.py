def ban(lev,lst,cb_lst,result):
    if lev == len(lst):
        result= sorted(result)
        if result not in cb_lst:
            cb_lst.append(result)
        return
    for i in lst[lev]:
        if i not in result:
            result.append(i)
            ban(lev+1,lst,cb_lst,result)
            result.remove(i)
    return cb_lst
    

def solution(user_id, banned_id):
    answer = 0
    cb_ban = []
    for i in banned_id:
        lst = []
        for j in user_id:
            flag=0
            if len(j)==len(i):
                for k in range(len(j)):
                    if j[k] == i[k] or i[k]=='*':
                        continue
                    else:
                        flag =1
                if flag != 1:
                    lst.append(j)
        cb_ban.append(lst)
        a = []
        b = []
        answer=len(ban(0,cb_ban,a,b))
    return answer
