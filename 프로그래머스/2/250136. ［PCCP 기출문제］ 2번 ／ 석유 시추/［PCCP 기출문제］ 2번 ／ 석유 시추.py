from collections import deque

def solution(land):
    # 1. BFS로 접근한다.
    # 2. 해당 컴포넌트가 존재하는 열 인덱스를 모아둔다.
    
    n = len(land)
    m = len(land[0])
    visited = [[False]*m for i in range(n)]
    pos = [0]*m # 각 열의 컴포넌트 계산
    
    delta = [(-1,0),(1,0),(0,-1),(0,1)]
    def bfs(i, j):
        q = deque([[i, j]])
        amount = 0
        width = set()
        
        while q:
            x, y = q.popleft()
            amount += 1
            width.add(y)
            
            for delta_x, delta_y in delta:
                new_x, new_y = x + delta_x, y + delta_y
                if 0 <= new_x < n and 0 <= new_y < m and land[new_x][new_y] and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    q.append([new_x, new_y])
            
        for w in width:
            pos[w] += amount
            
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and land[x][y]:
                visited[x][y] = True
                bfs(x, y)
    
    return max(pos)