#leet code 344.Reverse String
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) % 2 == 0 : #짝수
            center = len(s) // 2
        else : #홀수
            center = (len(s)-1) // 2
        
        for i in range(center): #처음부터 시작하는 i, 끝부터 시작하는 j (two pointer)
            j = (len(s)-1) - i
            s[i], s[j] = s[j], s[i]
            
