class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h_map = set()
        l, r = 0, 0
        count = 0
        maxCount = 0
        while l < len(s) and r < len(s):
            if s[r] in h_map:
                while l < len(s):
                    h_map.remove(s[l])
                    count -= 1
                    l += 1
                    if s[l-1] == s[r]: break
            else:
                h_map.add(s[r])
                r += 1
                count += 1
                maxCount = max(maxCount, count)
        return maxCount
