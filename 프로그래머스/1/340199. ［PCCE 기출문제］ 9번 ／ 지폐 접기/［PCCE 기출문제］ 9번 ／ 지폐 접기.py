def solution(wallet, bill):
    min_bill, max_bill = min(bill), max(bill)
    min_wallet, max_wallet = min(wallet), max(wallet)
    
    answer = 0
    while (min_bill > min_wallet) or (max_bill) > (max_wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
        min_bill, max_bill = min(bill), max(bill)
        
    return answer