import copy

N = int(input())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

def cal_score(team):
    score = 0
    for i in team:
        set_team = set(team)
        set_i = set([i])
        check_team = list(set_team - set_i)
        for c in check_team:
            score += arr[i-1][c-1]
    
    return score

# 가능한 팀 조합 만들기
total = []
ans = []
def dfs(s, team):

    ans.append(s)

    if len(ans) == team:
        total.append(copy.deepcopy(ans))
        ans.pop(-1)
        return

    for i in range(s+1, N+1):
        dfs(i, team)
    
    team -= 1
    ans.pop(-1)

dfs(1, N//2)

# 반대편 팀 조합 만들기
t = set([i for i in range(1, N+1)])
total_b = []
for a in total:
    b = list(t - set(a))
    total_b.append(b)

# 점수 계산하기
last = []
for i in range(len(total)):
    last.append(abs(cal_score(total[i]) - cal_score(total_b[i])))

print(min(last))