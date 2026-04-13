class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        new_s2 = s1[len(s1)//2:] + s2 + s1[:len(s1)//2]
        if new_s2 == s3:
            return True
        else:
            return False