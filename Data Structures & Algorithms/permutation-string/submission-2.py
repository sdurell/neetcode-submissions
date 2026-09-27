class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # turn s1 into list
        s1 = list(s1)

        l = 0
        for r, char in enumerate(s2):
            if char not in s1 and l == r:
                l += 1
            elif char not in s1:
                while char not in s1:
                    s1.append(s2[l])
                    l += 1
            if char in s1:
                s1.remove(char)

            if len(s1) == 0:
                return True
        
        return False
