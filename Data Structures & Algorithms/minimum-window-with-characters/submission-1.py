class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        haveCount = 0
        need = Counter(t)
        l = 0
        res = [0,float('inf')]
        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] = have.get(s[r], 0) + 1
                if have[s[r]] == need[s[r]]:
                    haveCount += 1
                while haveCount == len(need.values()):
                    if r - l < res[1] - res[0]:
                        res[0], res[1] = l, r
                    if s[l] in need:
                        have[s[l]] -= 1
                        if have[s[l]] < need[s[l]]:
                            haveCount -= 1
                    l += 1
        if res[1] == float('inf'):
            return ""
        return s[res[0]:res[1]+1]
