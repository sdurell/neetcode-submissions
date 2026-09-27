class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def backtrack(nums, subset):
            if subset not in self.res:
                self.res.append(subset.copy())
            if not nums:
                return
            subset.append(nums[0])
            backtrack(nums[1:], subset.copy())
            subset.pop()
            backtrack(nums[1:], subset.copy())

        backtrack(nums, [])
        return self.res