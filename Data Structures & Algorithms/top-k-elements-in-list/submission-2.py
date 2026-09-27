class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h_map = {}
        for n in nums:
            h_map[n] = h_map.get(n, 0) + 1
        
        freqs = sorted(h_map.items(), reverse=True, key=lambda x: x[1])

        return [f[0] for f in freqs[:k]]
