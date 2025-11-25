from collections import deque

N = int(input())
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

def check_in(x, y):
    if 0<=x<N and 0<=y<N:
        return True
        
def bfs(x, y, rain):
    q = deque()
    q.append((x,y))
    v[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            nx, ny = cx + dx, cy + dy
            if check_in(nx, ny) and arr[nx][ny] > rain and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = 1

ans = []
for rain in range(0, 100):
    cnt = 0
    v = [[0]*N for i in range(N)]
    for x in range(N):
        for y in range(N):
            if v[x][y] == 0 and arr[x][y] > rain:
                cnt += 1
                bfs(x,y,rain)

    ans.append(cnt)

print(max(ans))