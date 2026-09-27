class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            count = len(string)
            count = str(count)
            while len(count) < 3:
                count = "0" + count
            res += ("#" + count)
            res += string
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            if s[i] == "#":
                count = s[i + 1:i + 4]
                i += 4
                res.append(s[i: i + int(count)])
                i += int(count)
        return res
                