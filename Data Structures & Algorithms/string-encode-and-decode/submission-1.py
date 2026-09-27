class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            count = len(string)
            res += (str(count) + "#" + string)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        count = ""
        while i < len(s):
            if s[i] == "#":
                res.append(s[i+1:i+1+int(count)])
                i += 1 + int(count)
                count = ""
                continue
            count += s[i]
            i += 1    
        return res