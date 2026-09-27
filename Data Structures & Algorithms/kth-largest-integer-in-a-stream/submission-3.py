class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.data, self.k = nums, k

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        if len(self.data) > self.k:
            heapq.heappop(self.data)
        return self.data[0]
