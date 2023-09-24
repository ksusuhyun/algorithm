#leet code 728.Self Dividing Numbers

def selfDividingNumbers(left, right) :
    res = []
    
    for i in range(left,right+1):
        i_str = list(str(i))
    
        if '0' in i_str :
            pass
    
        else: 
            cnt = 0
            for j in i_str:
                if i % int(j) != 0 :
                    cnt += 1
            
            if cnt == 0 :
                res.append(i)

    return res

