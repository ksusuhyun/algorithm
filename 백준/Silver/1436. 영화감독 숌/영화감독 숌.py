target = int(input())
cnt = 1
num = 666

while cnt != target:
    num += 1
    str_num = str(num)
    for i in range(0,len(str_num)-2):
        if str_num[i:i+3] == '666':
            cnt += 1
            break
print(num)