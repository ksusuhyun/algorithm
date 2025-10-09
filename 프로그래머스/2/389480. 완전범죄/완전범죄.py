def solution(info, n, m):
    # info를 (a,b) 형태로 다시 저장
    ab_score = []
    for item in info:
        ab_score.append([[0, item[1]], [item[0], 0]])
    
    # 현재 선택지에서 다음 선택지를 더한다
    # 현재 코드에서 now가 2배씩 늘어나는 게 문제, 가지치기를 더해야 한다
    # 해결1. 중복되는 (a, b)는 저장하지 말자 => 시간초과 20개에서 3개로 줄임
    # 해결2. 해결1에서 not in list를 썼는데, 이거 말고 튜플로 (a,b)를 넣고 set을 쓰자
    
    # 예외 케이스 물건이 1개일 때
    if len(info) == 1:
        if info[0][1] < m:
            return 0
        elif info[0][0] < n:
            return info[0][0]
        else:
            return -1
        
    idx = 0
    now = ab_score[idx]
    while idx < len(info)-1:
        new_now = []
        for i in range(len(now)):
            for j in range(2):
                new_a = now[i][0] + ab_score[idx+1][j][0] # new a
                new_b = now[i][1] + ab_score[idx+1][j][1] # new b
                
                if (new_a < n and new_b < m):
                    new_now.append((new_a, new_b))
        now = list(set(new_now))
        idx += 1
        
    if len(new_now) == 0:
        return -1
    else:
        new_now = sorted(new_now, key=lambda x:x[0])
        return new_now[0][0]