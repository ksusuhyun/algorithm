def solution(id_list, report, k):
    n = len(id_list)
    id = {name:i for i, name in enumerate(id_list)}
    report_count = [[0]*n for i in range(n)]
    
    for r in report:
        nm1, nm2 = r.split()
        nm1_idx, nm2_idx = id[nm1], id[nm2]
        report_count[nm1_idx][nm2_idx] = 1
    
    report_result = []
    for i in range(n):
        report_result.append(sum([k[i] for k in report_count]))
    print(report_result)
    
    target_idx = []
    for i, res in enumerate(report_result):
        if res >= k:
            target_idx.append(i)
            
    answer = []
    for row in report_count:
        cnt = 0
        for t in target_idx:
            if row[t] == 1:
                cnt += 1
        answer.append(cnt)
    
    return answer