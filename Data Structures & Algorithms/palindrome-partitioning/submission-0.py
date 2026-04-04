class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start, len(s)):
                part = s[start:end+1]
                if is_palindrome(part):
                    path.append(part)
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        return res