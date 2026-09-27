class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for key in freq.keys():
            arr[freq[key]].append(key)
        res = []
        for l in reversed(arr):
            while l and k:
                res.append(l.pop())
                k -= 1
        return res