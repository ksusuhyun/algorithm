#leet code 125.Valid Palindrome

#import string 

#class Solution:
    #def isPalindrome(self, s: str) -> bool:
        #for i in string.punctuation: #문자열 내 모든 특수문자 제거
            #s = s.replace(i, "")
    
        #s = s.lower() #문자열을 소문자로 변경
        #s = s.replace(" ", "") #문자열 내 공백 제거
        
        #if s == s[::-1] :
            #return True
        #else :
            #return False

#print(isPalindrome("race a car"))


#문자열은 remove()를 사용할 수 없다.
#대신 문자열 내 문자를 제거하기 위해 strip, replace를 사용한다.
#split과 join 다시 공부하기
#공백을 제거하지 않으면 팰린드롬인지 확인 불가
#wings101 은 주피터와 다르게 print문이 필요하다.

s = 'a pin have cake'
s1 = s.split('e') #리스트로 저장
print(s1)
print(type(s1))
ss = ''.join(s1)
print(ss)
sss = 'm'.join(s)
print(sss)
print(type(sss))