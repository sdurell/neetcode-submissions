class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
                bucket[1].append(n)
            else:
                bucket[freq[n]].remove(n)
                freq[n] += 1
                bucket[freq[n]].append(n)
        
        res = []

        for f in range(len(bucket) - 1, 0, -1):
            for n in bucket[f]:
                res.append(n)

                if len(res) == k:
                    return res

        return res