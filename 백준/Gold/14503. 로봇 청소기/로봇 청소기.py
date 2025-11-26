N, M = map(int, input().split())
sx, sy, sr = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(cx,cy,cr):
    cnt = 0
    while True:
        # 현재 위치가 청소가 안 된 칸이라면 청소한다
        if arr[cx][cy] == 0:
            arr[cx][cy] = 2
            cnt += 1
        
        flag = True
        while flag:
            # 현재 위치 기준 왼쪽부터 4방향을 탐색하는데
            for nr in [(cr+3)%4, (cr+2)%4, (cr+1)%4, cr]:
                nx, ny = cx+dx[nr], cy+dy[nr]
                # 청소 안 된 칸을 만나면 그 칸을 현재 위치로 만들고 처음으로 돌아간다
                if arr[nx][ny] == 0:
                    cx, cy, cr = nx, ny, nr
                    flag = False
                    break
            
            # 4방향에 청소 안 된 칸이 없다면
            # 현재 방향(cr)을 유지해서 뒤쪽을 확인한다
            # 어차피 뒤쪽은 청소 안 된 칸이므로 굳이 현재 while문을 나가서 처음으로 돌아갈 필요는 없다
            else:
                nx, ny = cx-dx[cr], cy-dy[cr]
                if arr[nx][ny] == 1:
                    return cnt
                else:
                    cx, cy = nx, ny

print(solve(sx,sy,sr))
