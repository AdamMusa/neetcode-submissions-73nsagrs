class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(c.lower() for c in s if c.isalnum())
        return new_s == new_s[::-1]