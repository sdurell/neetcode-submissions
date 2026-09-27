class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        res = 0

        l, r = 0, 0
        while r < len(s):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)

            while (r - l + 1) - max(freqMap.values()) > k:
                freqMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res    
