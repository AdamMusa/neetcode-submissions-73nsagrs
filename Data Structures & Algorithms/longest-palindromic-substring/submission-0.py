class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        def expand(left: int, right: int) -> None:
            nonlocal res, res_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left +1
                if current_len > res_len:
                    res = s[left:right +1]
                    res_len = current_len
                left -=1
                right +=1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        return res
