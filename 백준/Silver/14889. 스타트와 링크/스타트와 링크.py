N = int(input())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

def cal(alst, blst):

    asm = 0
    for i in alst:
        for j in alst:
            asm += arr[i][j]

    bsm = 0
    for i in blst:
        for j in blst:
            bsm += arr[i][j]

    return abs(asm-bsm)

def dfs(n, alst, blst):
    global ans

    if n == N:
        # 각 팀이 똑같은 인원으로 나눠지면
        if len(alst) == len(blst):
            ans = min(ans, cal(alst, blst))
        return
    
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])
    
ans = float('inf')
dfs(0, [], [])

print(ans)