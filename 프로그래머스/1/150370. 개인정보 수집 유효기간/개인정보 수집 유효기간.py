def solution(today, terms, privacies):
    
    def int_to_str(num):
        if len(str(num)) == 1:
            num = f'0{num}'
        else:
            num = str(num)
        return num
            
    def count_term(time, term):
        y, m, d = time.split('.')
        # 나머지 연산을 위해 -1을 빼줌으로써
        # 1~12 체계를 0~11 체계로 바꿔준다
        y, m, d = int(y)-1, int(m)-1, int(d)-1
        
        day = term*28
        
        # 0~11 체계의 결과를 1을 더해줌으로써
        # 1~12 체계의 결과로 바꾼다
        dd = (d + day) % 28 + 1
        next_mon = (d + day) // 28 

        mm = (m + next_mon) % 12 + 1
        next_year = (m + next_mon) // 12

        yy = (y + next_year) + 1
        
        # 현재 어떤 날짜에도 00으로 끝나는 날은 없다
        # 전날 날짜 계산
        if (dd - 1) != 0:
            dd -= 1
        elif (dd - 1) == 0:
            dd = 28
            mm -= 1
            if mm == 0:
                mm = 12
                yy -= 1
                
        return int(str(yy)+int_to_str(mm)+int_to_str(dd))
    
    
    # 오늘 날짜를 숫자로 변경 ex) 20220519
    today_y, today_m, today_d = today.split('.')
    today = int(today_y+today_m+today_d)
    
    # terms dict으로 변경
    terms_dict = {}
    for i in terms:
        name, term = i.split()
        terms_dict[name] = int(term)
    
    print(terms_dict)
    # 조건 계산
    answer = []
    for i, pri in enumerate(privacies):
        time, term = pri.split()
        next_time = count_term(time, terms_dict[term])
        print(next_time)
        if next_time < today:
            answer.append(i+1)

    return answer