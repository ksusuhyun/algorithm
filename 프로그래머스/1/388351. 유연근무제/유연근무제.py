def solution(schedules, timelogs, startday):
    
    # 59를 넘으면 100자리가 올라가야 한다
    for i in range(len(schedules)):
        h = schedules[i] // 100
        m = schedules[i] % 100
        
        print(h, m)
        
        if m + 10 >= 60:
            h += 1
            m = (m+10) - 60
            
        else:
            m += 10
            
        schedules[i] = h*100 + m
        
    day_dict = {1:[0,1,2,3,4],
               2:[0,1,2,3,6],
               3:[0,1,2,5,6],
               4:[0,1,4,5,6],
               5:[0,3,4,5,6],
               6:[2,3,4,5,6],
               7:[1,2,3,4,5]}
    day_check = day_dict[startday]
    
    point = True
    answer = 0
    for j in range(len(schedules)):
        for k in day_check:
            if timelogs[j][k] > schedules[j]:
                point = False
                break
        if point:
            answer += 1
        point = True
        
    return answer