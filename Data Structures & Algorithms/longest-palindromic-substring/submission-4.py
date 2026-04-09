class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        best_start = 0
        best_len = 1
        i = 0

        while i < n:
            left = i
            right = i

            # 1) Merge duplicate chars to handle even-length centers cleanly
            while right + 1 < n and s[right] == s[right + 1]:
                right += 1

            # Skip this whole block next time
            i = right + 1

            # 2) Expand around the whole block
            while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            current_len = right - left + 1
            if current_len > best_len:
                best_start = left
                best_len = current_len

        return s[best_start:best_start + best_len]