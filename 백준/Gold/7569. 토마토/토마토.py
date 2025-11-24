from collections import deque

# 가로가 M, 세로가 N => M이 y, N이 x
M, N, H = map(int, input().split())
arr3d = [[] for i in range(H)]

for i in range(N*H):
    row = list(map(int, input().split()))
    arr3d[i//N].append(row)

v = [[[0]*M for j in range(N)] for i in range(H)]
d = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]

def check_in(z, x, y):
    if 0<=z<H and 0<=x<N and 0<=y<M:
        return True

def bfs():
    cnt = 0
    q = deque()

    for h in range(H):
        for x in range(N):
            for y in range(M):
                # 익은 토마토는 큐의 초기값으로 넣는다
                if arr3d[h][x][y] == 1:
                    q.append((h,x,y))
                    v[h][x][y] = 1
                # 안 익은 토마토의 개수를 센다
                elif arr3d[h][x][y] == 0:
                    cnt += 1

    while q:
        cz, cx, cy = q.popleft()
        for dz, dx, dy in d:
            nz, nx, ny = cz+dz, cx+dx, cy+dy
            if check_in(nz, nx, ny) and arr3d[nz][nx][ny] == 0 and v[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                v[nz][nx][ny] = v[cz][cx][cy] + 1
                cnt -= 1
    
    # 마지막으로 꺼낸 거
    if cnt==0:
        return v[cz][cx][cy]-1
    else:
        return -1

ans = bfs()
print(ans)