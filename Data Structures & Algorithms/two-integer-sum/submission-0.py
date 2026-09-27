class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in diff:
                return [diff.get(x), i]
            else:
                diff[nums[i]] = i
        return
