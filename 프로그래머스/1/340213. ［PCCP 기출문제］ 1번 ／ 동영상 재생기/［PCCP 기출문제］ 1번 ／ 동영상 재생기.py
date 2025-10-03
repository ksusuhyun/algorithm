def solution(video_len, pos, op_start, op_end, commands):
    
    def change_str_num(time):
        m = int(time[0:2])
        s = int(time[3:5])
        total_s = m*60 + s
        
        return total_s
    
    def two_position(s):
        if len(s) == 1:
            s = f'0{s}'
        return s
        
    video_len = change_str_num(video_len)
    pos = change_str_num(pos)
    op_start = change_str_num(op_start)
    op_end = change_str_num(op_end)
    
    if op_start <= pos and pos <= op_end:
        pos = op_end
        
    for i in commands:
        if i == 'next':
            if pos + 10 < video_len:
                pos = pos + 10
            else:
                pos = video_len
        elif i == 'prev':
            if pos > 10:
                pos = pos - 10
            else:
                pos = 0
                
        if op_start <= pos and pos <= op_end:
            pos = op_end
                
    h = two_position(str(pos//60))
    m = two_position(str(pos%60))
    
    answer = f'{h}:{m}'
    return answer