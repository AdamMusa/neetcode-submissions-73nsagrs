class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openP = {')':'(', '}': '{', ']':'['}
        for c in s:
            if c in openP:
                if stack and stack[-1] == openP[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False