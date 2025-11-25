N, M = map(int, input().split())
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

def after(arr):
    q = []
    new_arr = [[0]*M for i in range(N)]
    for x in range(N):
        for y in range(M):
            if arr[x][y] >= 1:
                q.append((x,y))
    while q:
        cx, cy = q.pop(0)
        cnt = 0
        for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                cnt += 1
        a = arr[cx][cy] - cnt 
        new_arr[cx][cy] = a if a > 0 else 0

    return new_arr 

def bfs(x,y,arr,v):
    q = []
    q.append((x,y))
    v[x][y] = 1

    while q:
        cx, cy = q.pop(0)
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] >= 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = 1

def check(arr):
    v = [[0]*M for i in range(N)]

    cnt = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] >= 1 and v[x][y] == 0:
                bfs(x,y,arr,v)
                cnt += 1
    return cnt

cnt = 0
while True:
    new_arr = after(arr)

    cnt += 1

    if check(new_arr) >= 2:
        print(cnt)
        break
    elif sum([sum(r) for r in new_arr]) == 0:
        print(0)
        break

    # 이걸 까먹다니...
    arr = new_arr