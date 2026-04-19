class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n1 = len(s1)
        for i in range(len(s2) - n1 + 1):
            subStr = s2[i: i + n1]
            subStr = sorted(subStr)
            if subStr == s1:
                return True
        return False