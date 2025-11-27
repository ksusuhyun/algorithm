import copy

N = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))

# 반례
# 식의 결과가 음수일 수 있는데
# max 계산에서 0으로 처리 됨

# max_ans = 0
# min_ans = float('inf')

max_ans = -1e10
min_ans = 1e10

def c(num1, num2, idx):
    if idx == 0:
        new = num1 + num2
    elif idx == 1:
        new = num1 - num2
    elif idx == 2:
        new = num1 * num2
    else:
        if num1 < 0:
            new = -((-num1)//num2)
        else:
            new = num1 // num2

    return new

def dfs(n, cal, s):
    global max_ans, min_ans

    if n == N-1:
        max_ans = max(max_ans, s)
        min_ans = min(min_ans, s)
        return
    
    for i in range(len(cal)):
        if cal[i] >= 1:
            new_cal = copy.deepcopy(cal)
            new_cal[i] -= 1
            dfs(n+1, new_cal, c(s, arr[n+1], i))

dfs(0, cal, arr[0])
print(max_ans)
print(min_ans)