N = int(input())
arr = []
for i in range(N):
    row = list(map(int, input()))
    arr.append(row)

v = [[0]*N for i in range(N)]
d = [(-1,0), (1,0), (0,-1), (0,1)]

def check_in(x,y):
    if 0<=x<N and 0<=y<N:
        return True

def bfs(x,y):
    global cnt, cnt_home

    q = []
    q.append((x,y))
    v[x][y] = cnt
    cnt_home += 1

    while q:
        c_x, c_y = q.pop(0)
        for d_x, d_y in d:
            new_x, new_y = c_x + d_x, c_y + d_y
            if check_in(new_x, new_y) and arr[new_x][new_y] and not v[new_x][new_y]:
                q.append((new_x, new_y))
                v[new_x][new_y] = cnt
                cnt_home += 1

# arr의 모든 곳을 돌자
cnt = 0
ans = []
for x in range(N):
    for y in range(N):
        if arr[x][y] and not v[x][y]:
            cnt += 1
            cnt_home = 0
            bfs(x, y)
            ans.append(cnt_home)

print(cnt)
ans.sort()
for a in ans:
    print(a)
