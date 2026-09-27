class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            leftover = x - y
            if leftover:
                heapq.heappush(stones, -leftover)
        return -stones[0] if stones else 0 