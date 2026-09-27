class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(count, subset, mask):
            if count >= len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if mask[i] == 1:
                    continue
                subset.append(nums[i])
                mask[i] = 1
                dfs(count + 1, subset, mask)
                subset.pop()
                mask[i] = 0
        
        mask = [0 for i in range(len(nums))]
        dfs(0, [], mask)
        return res