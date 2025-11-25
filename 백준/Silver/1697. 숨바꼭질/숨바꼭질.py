from collections import deque

N, K = map(int, input().split())

def bfs(s, e):
    q = deque()
    v = [0]*200000

    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return v[c]

        for d in (-1, 1, 2):
            if abs(d) == 1:
                n = c + d
            else:
                n = c * d
            if 0<=n<200000 and v[n]==0:
                v[n] = v[c] + 1
                q.append(n)

print(bfs(N, K)-1)