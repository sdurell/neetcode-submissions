class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        s1Map = Counter(s1)
        s2Map = {}
        for r in range(len(s2)):
            rightChar = s2[r]
            s2Map[rightChar] = s2Map.get(rightChar, 0) + 1
            if r - l + 1 > len(s1):
                leftChar = s2[l]
                s2Map[leftChar] -= 1
                if s2Map[leftChar] == 0:
                    del s2Map[leftChar]
                l += 1
            if s1Map == s2Map:
                return True
        return False
