class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = (l + r) // 2
            total = 0
            for num in piles:
                total += math.ceil(num / k)
            
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res