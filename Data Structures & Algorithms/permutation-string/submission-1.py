class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # turn s1 into list
        s1 = list(s1)

        l = 0
        for r, char in enumerate(s2):
            print(char)
            if char not in s1 and l == r:
                l += 1
                print(1)
            elif char not in s1:
                while char not in s1:
                    s1.append(s2[l])
                    l += 1
                    print(2)
            if char in s1:
                s1.remove(char)
                print(3)
            
            print(s1)

            if len(s1) == 0:
                return True
        
        return False
