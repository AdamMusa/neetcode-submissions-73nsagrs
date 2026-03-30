class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for char in strs:
            count = [0]*26
            for c in char:
                count[ord(c) - ord('a')] +=1
            key = tuple(count)
            res.setdefault(key, []).append(char)
        return list(res.values())