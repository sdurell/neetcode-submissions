class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal = max(piles)
        minK = float("inf")

        low, high = 1, maxVal
        if len(piles) == h:
            return maxVal

        while low <= high:
            k = (high - low) // 2 + low
            count = 0

            for num in piles:
                count += math.ceil(num / k)
                if count > h:
                    break

            if count > h:
                low = k + 1
            elif k <= minK:
                high = k - 1
                minK = k
        
        return minK


            
                    



