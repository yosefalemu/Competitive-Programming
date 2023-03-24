class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        sign = 1
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '+':
                res += sign * num
                num = 0
                sign = 1
            elif s[i] == '-':
                res += sign * num
                num = 0
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        return res + sign * num
        