class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        maxWindow = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        num, index = heap[0]
        maxWindow.append(-num)
        # l can be kept by r - k
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            num, index = heap[0]
            while index < r - k + 1:
                heapq.heappop(heap)
                num, index = heap[0]
            maxWindow.append(-num)
        return maxWindow