N = int(input())
ts = [0]*(N+1)
ps = [0]*(N+1)
for i in range(1, N+1):
    t, p = map(int, input().split())
    ts[i] = t
    ps[i] = p

def dfs(n, sm):
    global ans

    if n >= N+1:
        ans = max(ans, sm)
        return
    
    # 상담 한다와 상담 안 한다를 호출하는데
    # 상담 하는 경우는 조건이 붙는다
    # if-else로 쓰면 안 됨
    if n+ts[n] <= N+1:
        dfs(n+ts[n], sm+ps[n])
    dfs(n+1, sm)

ans = 0
dfs(1, 0)
print(ans)
