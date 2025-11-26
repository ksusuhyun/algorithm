# 각 반에 총감독관 1명은 무조건 필요하다

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for a in A:
    rest = a - B
    cnt += 1
    if rest > 0:
        if rest % C:
            cnt += (rest//C)+1
        else:
            cnt += (rest//C)

print(cnt)

