class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_map = set(nums)

        max_seq = 0
        for n in nums:
            local_max = 0
            while n in h_map:
                local_max += 1
                max_seq = max(local_max, max_seq)
                n -= 1
        
        return max_seq