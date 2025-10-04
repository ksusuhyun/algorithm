def solution(data, ext, val_ext, sort_by):
    col_dict = {'code':0,
               'date':1,
               'maximum':2,
               'remain':3}
    
    val_idx = col_dict[ext]
    sort_idx = []
    for row in range(len(data)):
        if data[row][val_idx] < val_ext:
            sort_idx.append(row)
    
    ori_dict = {}
    sort_col_idx = col_dict[sort_by]
    result = []
    for idx in sort_idx:
        result.append(data[idx][sort_col_idx])
        ori_dict[data[idx][sort_col_idx]] = idx
    
    result = sorted(result)
    answer = []
    for res in result:
        answer.append(data[ori_dict[res]])
        
    return answer