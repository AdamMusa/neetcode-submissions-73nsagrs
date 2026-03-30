class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenT = {}
        seenS = {}
        
        if len(t) != len(s):
            return False

        for i in range(0,len(s)):
            seenT[t[i]] = 1 + seenT.get(t[i], 0)
            seenS[s[i]] = 1 + seenS.get(s[i], 0)
                
        return seenT == seenS
        