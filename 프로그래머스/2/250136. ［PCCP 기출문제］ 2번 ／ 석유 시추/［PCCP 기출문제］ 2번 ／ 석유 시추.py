from collections import deque

def solution(land):
    n, m = len(land), len(land[0])

    # 컴포넌트 id 기록(-1은 물)
    comp = [[-1]*m for _ in range(n)]
    sizes = []  # sizes[cid] = 해당 컴포넌트 크기

    DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

    def bfs(sx, sy, cid):
        q = deque([(sx, sy)])
        comp[sx][sy] = cid
        cnt = 1
        while q:
            x, y = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if land[nx][ny] == 1 and comp[nx][ny] == -1:
                        comp[nx][ny] = cid
                        cnt += 1
                        q.append((nx, ny))
        return cnt

    # 1) 모든 덩어리 라벨링 + 크기 저장
    cid = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and comp[i][j] == -1:
                size = bfs(i, j, cid)
                sizes.append(size)
                cid += 1

    # 2) 각 열마다 만난 컴포넌트 id를 set으로 모아 중복 없이 합산
    ans = 0
    for col in range(m):
        seen = set()
        total = 0
        for row in range(n):
            c = comp[row][col]
            if c != -1 and c not in seen:
                seen.add(c)
                total += sizes[c]
        ans = max(ans, total)

    return ans
