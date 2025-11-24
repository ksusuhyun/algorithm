N, M = map(int, input().split())
arr = []
for i in range(N):
    row = list(map(int, input()))
    arr.append(row)

v = [[0]*M for i in range(N)]

d = [(-1,0), (1,0), (0,-1), (0,1)]

def check_in(x, y):
    if 0<=x<N and 0<=y<M:
        return True

def bfs(sx, sy, ex, ey):
    q = []
    q.append((sx,sy))
    v[sx][sy] = 1

    while q:
        c_x, c_y = q.pop(0)

        # 정답 조건 처리
        if (c_x, c_y) == (ex, ey):
            return v[c_x][c_y]

        for d_x, d_y in d:
            new_x, new_y = c_x + d_x, c_y + d_y
            if check_in(new_x, new_y) and arr[new_x][new_y] and not v[new_x][new_y]:
                q.append((new_x, new_y))
                v[new_x][new_y] = v[c_x][c_y] + 1

print(bfs(0, 0, N-1, M-1))