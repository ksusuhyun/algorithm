#leet code 125.Valid Palindrome

import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in string.punctuation: #문자열 내 모든 특수문자 제거
            s = s.replace(i, "")
    
        s = s.lower() #문자열을 소문자로 변경
        s = s.replace(" ", "") #문자열 내 공백 제거
        
        if s == s[::-1] :
            return True
        else :
            return False
