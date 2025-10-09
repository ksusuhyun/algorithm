from itertools import combinations

def solution(n, q, ans):
    num_list = [i for i in range(1,n+1)]
    all_com = list(combinations(num_list, 5))
    
    for idx, input in enumerate(q):
        new_all_com = []
        for com in all_com:
            com = set(com)
            set_input = set(input)
            
            if len(list(com & set_input)) >= ans[idx]:
                new_all_com.append(com)
        all_com = new_all_com
        
    # 마지막으로 모든 입력한 정수와의 교집합이 같지 않으면 제거한다
    for idx, input in enumerate(q):
        new_all_com = []
        for com in all_com:
            com = set(com)
            set_input = set(input)
            
            if len(list(com & set_input)) == ans[idx]:
                new_all_com.append(com)
        all_com = new_all_com
        
    # print(new_all_com)
    return len(new_all_com)