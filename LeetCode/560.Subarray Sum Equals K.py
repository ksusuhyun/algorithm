#leet code 560.Subarray Sum Equals K

def subarraySum(nums, k) :
    res = 0
    prefix_sum = 0
    
    for_k = {0:1}
    
    for num in nums :
        prefix_sum += num
    
        if prefix_sum - k in for_k :
            res += for_k[prefix_sum - k]
    
        if prefix_sum not in for_k :
            for_k[prefix_sum] = 1
        else :
            for_k[prefix_sum] += 1
    
    return res
