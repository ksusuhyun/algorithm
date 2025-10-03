def solution(n, w, num):
    
    # 구조 만들기
    totallist = []
    sublist = []
    for i in range(1, n+1):
        if i % w == 0:
            sublist.append(i)
            if (i // w) % 2 == 0:
                sublist = sublist[::-1]
            totallist.append(sublist)
            sublist = []
        else:
            sublist.append(i)
            if i == n:
                if (i // w) % 2 != 0:
                    sublist = sublist[::-1]
                totallist.append(sublist)
            
    len_totallist_last = len(totallist[-1])
    len_totallist = len(totallist)
    
    if len_totallist_last != w:
        if len_totallist % 2 == 0:
            totallist[-1] = [0]*(w-len_totallist_last) + totallist[-1]
        else:
            totallist[-1] = totallist[-1] + [0]*(w-len_totallist_last)
    # print(totallist)
    
    # num 접근하기
    num_quot = num // w
    num_remain = num % w
    print(num_quot)
    print(num_remain)
    
    if num_remain == 0:
        start_layer = num_quot
        if num_quot % 2 == 0:
            idx = 0
        else:
            idx = -1
    else:
        start_layer = num_quot + 1
        if num_quot % 2 == 0:
            idx = num_remain - 1
        else:
            idx = w - num_remain

    # 답 찾기
    answer = 0
    for j in range(start_layer, len_totallist):
        if totallist[j][idx] != 0:
            answer += 1
            
    return answer + 1