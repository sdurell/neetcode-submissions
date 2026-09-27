class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if target - s > 0:
                l += 1
            elif target - s < 0:
                r -= 1
            else:
                return [l + 1, r + 1]