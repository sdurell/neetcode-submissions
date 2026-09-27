class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = high
        while low <= high:
            mid = (high - low) // 2 + low

            sumH = 0
            for pile in piles:
                sumH += math.ceil(pile / mid)
            if sumH <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1
        return k
                