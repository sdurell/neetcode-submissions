class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        minNum = float("inf")

        while low <= high:
            mid = (high + low) // 2
            minNum = min(minNum, nums[mid])

            if nums[high] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return minNum