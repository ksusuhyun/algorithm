S = []
for _ in range(4):
    S.append(list(map(int, input())))
K = int(input())
Ks = []
for _ in range(K):
    n, r = map(int, input().split())
    Ks.append((n,r))

def rotate(t, r):
    if r == -1:
        S[t-1] = S[t-1] + [0]
        S[t-1][-1] = S[t-1][0]
        S[t-1].pop(0)
    else:
        S[t-1] = [0] + S[t-1]
        S[t-1][0] = S[t-1][-1]
        S[t-1].pop(-1)

def bfs(s):
    q = []
    ans = []
    q.append(s)
    v[s[0]] = 1

    while q:
        cn, cr = q.pop(0)
        ans.append((cn,cr))
        for i in [-1, 1]:
            if 0<(cn+i)<5 and v[cn+i]==0:
                v[cn+i] = 1
                # 앞쪽의 오른쪽과 현재의 왼쪽 비교
                if i == -1:
                    if S[cn+i-1][2] != S[cn-1][6]:
                        q.append((cn+i, -cr))
                # 뒤쪽의 왼쪽과 현재의 오른쪽 비교
                else:
                    if S[cn+i-1][6] != S[cn-1][2]:
                        q.append((cn+i, -cr))

    return ans

for k in Ks:
    v = [0]*5
    new_k = bfs(k)
    for t, new_r in new_k:
        rotate(t, new_r)

sm = 0
for i in range(4):
    sm += S[i][0] * (2**i)

print(sm)
