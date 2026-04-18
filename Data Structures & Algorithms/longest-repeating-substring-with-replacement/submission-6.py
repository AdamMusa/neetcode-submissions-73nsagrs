class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        res = 0
        max_f = 0

        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            max_f = max(max_f, mp[s[r]])
            
            if (r - l + 1) - max_f > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res