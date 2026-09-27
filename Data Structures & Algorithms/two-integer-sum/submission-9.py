class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i, n in enumerate(nums):
            hMap[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hMap and i != hMap[diff]:
                return [i, hMap[diff]]