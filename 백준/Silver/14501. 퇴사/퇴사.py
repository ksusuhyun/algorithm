N = int(input())
ts = [0]*(N+1)
ps = [0]*(N+1)
for i in range(1, N+1):
    t, p = map(int, input().split())
    ts[i] = i+t
    ps[i] = p

def dfs(st):
    global cnt
    
    cnt += ps[st]

    for i in range(ts[st], N+1):
        if ts[i] <= (N+1):
            dfs(i) 
    
    ans.append(cnt)
    cnt -= ps[st]

last_ans = []
for i in range(1, N+1):
    if ts[i] <= (N+1):
        ans = []
        cnt = 0
        dfs(i)
        last_ans.append(max(ans))

# 반례 1
# 상담할 수 있는 날이 없어서 ans 리스트가 아예 비어있는 경우
if len(last_ans) == 0:
    print(0)
else:
    print(max(last_ans))