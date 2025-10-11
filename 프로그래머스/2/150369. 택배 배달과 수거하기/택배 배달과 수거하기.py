def solution(cap, n, deliveries, pickups):
    # 맨 마지막 집부터 가야한다는 걸 stack의 pop을 이용한다.
    idps = [(i,d,p) for i, (d, p) in enumerate(zip(deliveries, pickups), 1) if d or p]
    delivery = 0
    pickup = 0
    answer = 0
    while idps:
        i,d,p = idps.pop()
        delivery += d
        pickup += p
        # delivery, pickup이 양수라는 건 그 집까지 가야한다는 뜻
        # 음수라는 건 남아있다는 뜻, 그 집까지 가지 않아도 배달 수거가 가능하다
        while delivery>0 or pickup>0:
            delivery -= cap
            pickup -= cap
            answer += (2*i)
            
    return answer