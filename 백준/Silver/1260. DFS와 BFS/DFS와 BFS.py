N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

# 그래프 구현
for i in range(M):
    a, b = map(int, input().split())
    # 양방향
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것을 먼저 방문 -> 각 정점 오름차순 정렬
for node in graph:
    node = node.sort()

# DFS
def dfs(c):
    v[c] = 1
    ans_dfs.append(c)
    for n in graph[c]:
        if v[n] == 0:
            dfs(n)

# BFS
def bfs(s):
    q = []
    q.append(s)
    v[s] = 1
    ans_bfs.append(s)

    while q:
        c = q.pop(0)
        for n in graph[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = 1
                ans_bfs.append(n)

v = [0]*(N+1)
ans_dfs, ans_bfs = [], []
dfs(V)

v = [0]*(N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)