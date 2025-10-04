def solution(friends, gifts):
    
    # (nxn) 2차원 리스트 만들기
    n = len(friends)
    gift_count = []
    for row in range(n):
        gift_count.append([0]*n)
    
    name_dict = {}
    for i, name in enumerate(friends):
        name_dict[name] = i
        
    for log in gifts:
        name1, name2 = log.split()
        name1_idx, name2_idx = name_dict[name1], name_dict[name2]
        gift_count[name1_idx][name2_idx] += 1
        
    # 선물 지수 계산하기
    gift_score = {}
    for ga in range(n):
        g = sum(gift_count[ga])
        r = 0
        for se in range(n):
            r += gift_count[se][ga]
        gift_score[ga] = g - r
    
    print(gift_score)
    
    # 예측하기
    next_month = [0]*n
    for row in range(n):
        for col in range(row, n):
            if row == col:
                continue
            print(row, col)
            a = gift_count[row][col]
            b = gift_count[col][row]
            
            if a > b:
                next_month[row] += 1
            elif a < b:
                next_month[col] += 1
            else:
                a_gift_score = gift_score[row]
                b_gift_score = gift_score[col]
                
                if a_gift_score > b_gift_score:
                    next_month[row] += 1
                elif a_gift_score < b_gift_score:
                    next_month[col] += 1
    print(next_month)
    
    return max(next_month)