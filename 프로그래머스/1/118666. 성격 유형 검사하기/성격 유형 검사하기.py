def solution(survey, choices):
    
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    p = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i, s in enumerate(survey):
        f, s = s[0], s[1]
        if choices[i] <= 3:
            p[f] += score[choices[i]]
        elif choices[i] >= 5:
            p[s] += score[choices[i]]
    
    list1 = [p['R'], p['C'], p['J'], p['A']]
    list2 = [p['T'], p['F'], p['M'], p['N']]
    
    list1_name = ['R', 'C', 'J', 'A']
    list2_name = ['T', 'F', 'M', 'N']
    result = []
    for j in range(4):
        if list1[j] >= list2[j]:
            result.append(list1_name[j])
        else:
            result.append(list2_name[j])
    
    return f'{result[0]}{result[1]}{result[2]}{result[3]}'