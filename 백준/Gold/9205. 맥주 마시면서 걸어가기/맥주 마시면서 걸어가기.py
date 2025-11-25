def bfs(arr):

    n = len(arr)
    v = [0]*n
    q = []
    q.append(arr[0])
    v[0] = 1

    while q:
        cx, cy = q.pop(0)

        if (cx, cy) == arr[-1]:
            return 'happy'

        for i in range(n):
            if arr[i] != (cx, cy) and v[i] == 0 and abs(arr[i][0]-cx)+abs(arr[i][1]-cy) <= 1000:
                q.append(arr[i])
                v[i] = 1
    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())
    
    arr = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        arr.append((x, y))
    
    # arr에 대해 bfs
    print(bfs(arr))
