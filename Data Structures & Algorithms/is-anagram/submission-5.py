class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for char in s:
            if not s_map.get(char): s_map[char] = 1
            else: s_map[char] += 1

        for char in t:
            if not t_map.get(char): t_map[char] = 1
            else: t_map[char] += 1

        return s_map == t_map
