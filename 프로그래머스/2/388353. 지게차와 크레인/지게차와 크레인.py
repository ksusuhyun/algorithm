def solution(storage, requests):
    
    grid = [ list(row) for row in storage ]
    
    
    # 2차원 배열 접근
    def grid_search(grid, target):
        
        target_idx = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == target:
                    target_idx.append((i,j))
        return target_idx
    
    # 한 좌표의 4면을 확인하는 함수
    # 이 좌표는 창고의 외부와 닿아있다, 닿아있지 않다
    def check_4(grid, loc, visited=None):
        if visited is None:
            visited = set()

        n, m = len(grid), len(grid[0])
        x, y = loc

        # 이미 방문했으면 더 안 들어감
        if (x, y) in visited:
            return False
        visited.add((x, y))

        # 현재 위치가 테두리면 True
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            return True

        # 4방향 탐색
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                if check_4(grid, (nx, ny), visited):
                    return True

        return False

        
    # 지게차 함수 만들기
    def check(grid, target_idx):
        ok = []
        for idx in target_idx:
            out = check_4(grid, idx)
            if out:
                ok.append((idx[0],idx[1]))
        return ok

    for req in requests:
        if len(req) == 1:
            target_idx = grid_search(grid, req)
            print(target_idx)
            ok = check(grid, target_idx)
            print(ok)
            for k in ok:
                grid[k[0]][k[1]] = 0
        else:
            target_idx = grid_search(grid, req[0])
            for idx in target_idx:
                grid[idx[0]][idx[1]] = 0
    
    answer = 0
    for row in grid:
        for r in row:
            if str(r).isalpha():
                answer += 1
                
    return answer