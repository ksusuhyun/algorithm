N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

h, c = [], []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            h.append((x+1,y+1))
        elif arr[x][y] == 2:
            c.append((x+1,y+1))

row, col = len(h), len(c)
dis = [[0]*col for _ in range(row)]
for x in range(row):
    for y in range(col):
        dis[x][y] = abs(h[x][0]-c[y][0]) + abs(h[x][1]-c[y][1])

ans = float('inf')
def cal(idxlst):
    sm = 0
    for x in range(len(dis)):
        m = float('inf')
        for i in idxlst:
            m = min(m, dis[x][i])
        sm += m
    
    return sm

def dfs(idx, d, lst):
    global ans

    if idx >= col:
        if len(lst) == M:
            ans = min(ans, d)
        return

    dfs(idx+1, cal(lst+[idx]), lst+[idx])
    dfs(idx+1, d, lst)

dfs(0, 0, [])
print(ans)