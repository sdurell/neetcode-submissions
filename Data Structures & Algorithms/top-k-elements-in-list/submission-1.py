class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in freq.items():
            bucket[val].append(key)
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                print(bucket[i])
                for j in range(len(bucket[i])):
                    print(j)
                    if k > 0:
                        res.append(bucket[i][j])
                        k -= 1
        return res