#leet code 1480.Running Sum of 1d Array

def runningSum(nums):
     runningSum = []
     sum = 0
     for i in nums:
         sum += i
         runningSum.append(sum)
     return runningSum