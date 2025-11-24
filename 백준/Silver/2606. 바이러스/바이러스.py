N = int(input())
M = int(input())

# 인접 리스트 구현
adj = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(c):
    global cnt
    
    v[c] = 1
    for n in adj[c]:
        if v[n] == 0:
            cnt += 1
            dfs(n)

v = [0]*(N+1)
cnt = 0
dfs(1)
print(cnt)