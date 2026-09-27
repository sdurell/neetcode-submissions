class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for strng in strs:
            res.append(str(len(strng)))
            res.append("#")
            res.append(strng)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            num = []
            while s[i] != "#":
                num.append(s[i])
                i += 1
            num = int("".join(num))
            i += 1
            res.append(s[i: i + num])
            i += num
        return res
