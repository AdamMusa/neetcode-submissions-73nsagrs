class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        if not num2:
            return num1
        return str(int(num1)*int(num2))