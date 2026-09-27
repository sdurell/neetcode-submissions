class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        low, high = 0, len(nums) - 1
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break

            mid = (high - low) // 2 + low
            res = min(res, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return res
    