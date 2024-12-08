import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for i in range(int(sys.stdin.readline().rstrip())):
    cmd = sys.stdin.readline().rstrip()
    if cmd[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif cmd[0] == 'D' :
        if st2:
            st1.append(st2.pop())
    elif cmd[0] == 'B' :
        if st1:
            st1.pop()
    else:
        st1.append(cmd[2])

        
st1.extend(reversed(st2))
print(''.join(st1))
