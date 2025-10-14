import sys

n, m = map(int, input().split())

name = {}
digit = {}
for i in range(n):
    nm = sys.stdin.readline().rstrip()
    name[nm] = i+1
    digit[i+1] = nm

# list.index()가 for문 안에 들어가면서 O(n^2) 되어 시간 초과 발생
for j in range(m):
    inp = input()
    if inp.isdigit():
        print(digit[int(inp)])
    else:
        print(name[inp])