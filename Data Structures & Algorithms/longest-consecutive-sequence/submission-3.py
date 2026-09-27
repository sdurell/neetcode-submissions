class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxNum = 0
        h = set(nums)
        for num in nums:
            if num - 1 not in h:
                j = 0
                while num + j in h:
                    maxNum = max(maxNum, j + 1)
                    j += 1
        return maxNum 