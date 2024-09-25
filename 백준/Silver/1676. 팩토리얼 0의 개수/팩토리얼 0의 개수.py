N = int(input())

num = 1
for i in range(1,N+1):
    num *= i
    
cnt = 0
for j in list(str(num))[::-1]:
    if j == '0':
        cnt +=  1
    else:
        break

print(cnt)