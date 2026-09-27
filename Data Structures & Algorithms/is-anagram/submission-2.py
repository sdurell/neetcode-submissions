class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS, freqT = {}, {}
        for char in s:
            if freqS.get(char):
                freqS[char] += 1
            else:
                freqS[char] = 1 

        for char in t:
            if freqT.get(char):
                freqT[char] += 1
            else:
                freqT[char] = 1 
        
        return True if freqS == freqT else False