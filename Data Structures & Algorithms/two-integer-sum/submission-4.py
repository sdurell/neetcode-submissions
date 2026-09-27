class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {num: i for (i, num) in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if target - num in h_map and h_map[target-num] != i:
                return [i, h_map[target-num]]
        