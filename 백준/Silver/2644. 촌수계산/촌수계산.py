n = int(input())
f, s = map(int,input().split())
m = int(input())

adj = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

v = [0]*(n+1)

def bfs(s, e):
    global cnt

    q = []
    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        # 정답 처리는 이 위치에서 하는 게 편하다
        if c == e:
            return v[c]-1
        
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] += v[c] + 1

        cnt += 1

    return -1

cnt = 0
print(bfs(f, s))
