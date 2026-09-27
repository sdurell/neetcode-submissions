class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = set()
        for num in nums:
            if num in hMap:
                return True
            hMap.add(num)
        return False