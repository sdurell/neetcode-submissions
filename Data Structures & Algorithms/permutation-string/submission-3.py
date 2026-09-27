class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Freq, s2Freq = {}, {}
        for i in range(len(s1)):
            s1Freq[s1[i]] = 1 + s1Freq.get(s1[i], 0)
            s2Freq[s2[i]] = 1 + s2Freq.get(s2[i], 0)
        
        for r in range(len(s1), len(s2)):
            if s1Freq == s2Freq:
                return True
            l = r - len(s1)

            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0: 
                s2Freq.pop(s2[l])
            s2Freq[s2[r]] = 1 + s2Freq.get(s2[r], 0)
        
        return s1Freq == s2Freq    