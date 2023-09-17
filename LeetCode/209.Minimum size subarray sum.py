#leet code #209.Minimum size subarray sum

def minSubArrayLen(target, nums) :
    min_len = float('inf')
    left = 0
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        while (sum>=target):
            min_len = min(min_len,i+1-left)
            sum -= nums[left]
            left += 1
    if min_len != inf :
        return min_len
    else :
        return 0
    
    