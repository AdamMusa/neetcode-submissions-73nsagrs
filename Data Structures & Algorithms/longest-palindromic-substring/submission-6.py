class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        best_l = 0
        best_r = 0
        i = 0

        while i < n:
            l = i
            r = i

            # Build one center block: "a", "bb", "aaaa", etc.
            while r + 1 < n and s[r + 1] == s[l]:
                r += 1

            # Next iteration starts after this whole block
            i = r + 1

            # Expand around the block
            while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1

            if r - l > best_r - best_l:
                best_l = l
                best_r = r

        return s[best_l:best_r + 1]