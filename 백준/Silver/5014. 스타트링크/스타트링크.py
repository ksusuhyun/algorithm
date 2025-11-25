F, S, G, U, D = map(int, input().split())

def bfs(S,G):
    q = []
    v = [0]*(F+1)

    q.append(S)
    v[S] = 1

    while q:
        c = q.pop(0)
        if c == G:
            return v[c]-1

        for d in (+U, -D):
            n = c + d
            if 1<=n<=F and v[n]==0:
                q.append(n)
                v[n] = v[c] + 1
    
    return 'use the stairs'

print(bfs(S,G)) # S: 시작 층수, G: 목표 층수
