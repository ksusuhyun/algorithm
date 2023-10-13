#leet code 5.Longest Palindrome Substring

def longestPalindrome(s) :
        
    def expand(left,right):
        while left >= 0 and right < len(s) and s[left] == s[right] :
            left -= 1
            right += 1
        return right - left - 1
    
    if len(s) < 2 or s == s[::-1] :
        return s
    
    res = 0
    for i in range(len(s)-1) :
        res = max(res, expand(i,i+1), expand(i,i+2))
    
    return res
      