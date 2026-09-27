class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        res = []
        for i in range(len(strs)):
            sortedString = "".join(sorted(strs[i]))
            if sortedString in freq:
                res[freq[sortedString]].append(strs[i])
            else:
                freq[sortedString] = len(res)
                res.append([strs[i]])
        return res
        
