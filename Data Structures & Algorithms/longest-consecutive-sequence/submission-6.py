class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hMap = set(nums)
        maxLen = 0
        for n in nums:
            length = 1
            while n - 1 in hMap:
                length +=1
                n -= 1
            maxLen = max(maxLen, length)
        return maxLen