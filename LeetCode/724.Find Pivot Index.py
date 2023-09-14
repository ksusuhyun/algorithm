#leet code 724.Find Pivot Index
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = []
        for i in range(len(nums)):
            if sum(left) == sum(nums[i+1:]) :
                return i
            else :
                left.append(nums[i])
            
            if i == (len(nums)-1):
                return -1