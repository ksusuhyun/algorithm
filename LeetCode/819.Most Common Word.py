#leet code 819.Most Common Word
from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = re.sub('[^\w]',' ',paragraph) #전처리 과정
        para_list = para.lower().split()
        para_set = list(set(para_list))

        para_real = []
        for i in para_set:
            if i not in banned:
                para_real.append(i)

        res = {} 
        for j in para_real:
            cnt = para_list.count(j)
            res[j] = cnt
            
        max_cnt = max(res, key=res.get) #value가 최대일 때 key값
        return max_cnt
