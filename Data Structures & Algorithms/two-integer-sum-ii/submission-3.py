class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            k = numbers[l] + numbers[r]

            if k > target:
                r -= 1
            elif k < target:
                l += 1
            else:
                return [l+1, r+1]
