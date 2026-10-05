class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            res.append(f"{len(st)}#")
            res.append(st)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            numChars = ""
            while s[i] != "#":
                numChars += s[i]
                i += 1
            numCharsInt = int(numChars)
            # skip the #
            i += 1
            res.append(s[i:i + numCharsInt])
            i += numCharsInt
        return res