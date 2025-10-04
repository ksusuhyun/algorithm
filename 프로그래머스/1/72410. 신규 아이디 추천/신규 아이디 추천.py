def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    condition = []
    for i in range(10):
        condition.append(str(i))
    for j in range(97, 123):
        condition.append(chr(j))

    new_id_list = []
    for w in new_id:
        if w in ['-','_','.']:
            new_id_list.append(w)
        elif w in condition:
            new_id_list.append(w)
    
    # 3단계
    dot_idx = []
    for i, w in enumerate(new_id_list):
        if w == '.':
            dot_idx.append(i)
            
    for i in range(len(dot_idx)-1):
        if dot_idx[i+1] - dot_idx[i] == 1:
            new_id_list[dot_idx[i]] = '!'
            
    new_id_list_new = []
    for w in new_id_list:
        if w != '!':
            new_id_list_new.append(w)
            
    # 4단계
    if len(new_id_list_new) != 0 and new_id_list_new[0] == '.' :
        new_id_list_new = new_id_list_new[1:]
    if len(new_id_list_new) != 0 and new_id_list_new[-1] == '.' :
        new_id_list_new = new_id_list_new[:-1]
        
    # 5단계
    if len(new_id_list_new) == 0:
        new_id_list_new = ['a']
    
    # 6단계
    if len(new_id_list_new) >= 16:
        new_id_list_new = new_id_list_new[:15]
        if new_id_list_new[-1] == '.':
            new_id_list_new = new_id_list_new[:-1]
    
    # 7단계
    if len(new_id_list_new) <= 2:
        for i in range(3-len(new_id_list_new)):
            new_id_list_new.append(new_id_list_new[-1])
        
    print(''.join(new_id_list_new))
            
    return ''.join(new_id_list_new)