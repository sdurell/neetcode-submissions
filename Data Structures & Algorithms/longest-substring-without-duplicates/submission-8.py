class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h_map = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in h_map:
                h_map.remove(s[l])
                l += 1
            h_map.add(s[r])
            res = max(res, r - l + 1)
        return res