from itertools import product

def solution(users, emoticons):
    
    m = len(emoticons)
    
    # 가능한 모든 할인율 중복 순열
    discount = list(product([10,20,30,40], repeat=m))
    
    #
    result = set()
    for dis in discount:
        res = [0, 0]
        for user in users:
            user_dis, money = user[0], user[1]
            now = 0
            for idx, item_dis in enumerate(list(dis)):
                if item_dis >= user_dis:
                    d = emoticons[idx]*(item_dis*0.01)
                    now += int(emoticons[idx]-d)
            if now >= money:
                res[0] += 1
            else:
                res[1] += now
        result.add((res[0], res[1]))
        
    result = sorted(list(result), key=lambda x:(-x[0], -x[1]))
    
    return list(result[0])