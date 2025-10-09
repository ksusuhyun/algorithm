def solution(players, m, k):
    
    now_server = [0]*24
    cnt = [0]*24
    
    for idx, p in enumerate(players):
        need  = p // m
        if need > now_server[idx]:
            real_need = need - now_server[idx]
            for i in range(k):
                if (idx+i) < 24:
                    now_server[idx+i] += real_need
            cnt[idx] = real_need
        # print(now_server)
    
    print(cnt)
    return sum(cnt)