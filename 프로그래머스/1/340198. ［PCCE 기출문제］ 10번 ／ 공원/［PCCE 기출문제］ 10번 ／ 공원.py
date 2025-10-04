def solution(mats, park):
    
    num_row = len(park)
    num_col = len(park[0])
    mats = sorted(mats, reverse=True)
    print(mats)

    point = False
    for mat in mats:
        if point:
            break
        for row in range(num_row):
            if point:
                break
            for col in range(num_col):

                if (row + mat-1 > num_row-1) or (col + mat-1 > num_col-1):
                    break
                # 기준점
                print(row, col)

                point = True
                for next_row in range(row, row+mat):
                    if park[next_row][col:col+mat].count('-1') == mat:
                        continue
                    else:
                        point = False
                        break
                print(point)
                if point:
                    answer = mat
                    break
                
    if not point:
        answer = -1
    
    return answer