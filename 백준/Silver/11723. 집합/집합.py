# input()은 속도가 느리다
# sys.stdin.readline().rstrip()을 사용하자
# sys.stdin.readline()은 문자열을 입력으로 받는데, \n도 함께 받아서 rstrip()을 통해 제거할 필요가 있다
import sys

m = int(input())
S = set()
for i in range(m):
    # all, empty는 숫자 없이 명령만 주어진다
    ss = sys.stdin.readline().rstrip().split()
    if len(ss) == 2:
        s, num = str(ss[0]), int(ss[1])
    else:
        s = str(ss[0])
        
    if s == 'add':
        S.add(num)
    elif s == 'remove':
        S.discard(num)
    elif s == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif s == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    # 미리 정의한 S2로 S=S2 해 버리면
    # S가 S2를 가리키도록 바뀐다
    # 따라서 S.add(3)을 하면 S2.add(3)도 된다
    elif s == 'all':
        S = set([i for i in range(1,21)])
    else:
        S = set()