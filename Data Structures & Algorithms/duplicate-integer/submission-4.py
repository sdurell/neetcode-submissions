class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = set()
        for i in nums:
            if i in hMap:
                return True
            hMap.add(i)
        return False