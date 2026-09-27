class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            i = (high - low) // 2 + low
            if nums[i] > target:
                high = i - 1
            elif nums[i] < target:
                low = i + 1
            else:
                return i
        return -1