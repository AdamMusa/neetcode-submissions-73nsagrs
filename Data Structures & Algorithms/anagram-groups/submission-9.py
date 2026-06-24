class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for char in strs:
            sortedS = ''.join(sorted(char))
            res[sortedS].append(char)
        return list(res.values())