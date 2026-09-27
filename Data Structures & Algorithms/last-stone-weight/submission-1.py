class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]

        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x < y:
                x = y - x
            elif x > y:
                x = x - y
            else:
                x = 0
            heapq.heappush(stones, -x)
        if stones:
            return -heapq.heappop(stones)
        else:
            return 0
