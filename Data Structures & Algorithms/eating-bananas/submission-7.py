class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile / k)
            print(t, k)
            if t > h:
                l = k + 1
            elif t <= h:
                res = k
                r = k - 1
        return res