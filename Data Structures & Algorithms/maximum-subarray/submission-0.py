class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = max(nums)
        localSum = 0
        for n in nums:
            if localSum + n > 0:
                localSum += n
                maxVal = max(maxVal, localSum)
            else:
                localSum = 0
        
        return maxVal