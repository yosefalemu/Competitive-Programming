class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                tempStr = ""
                while stack[-1] != "[":
                    tempStr = stack.pop() + tempStr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*tempStr)
        return "".join(stack)
                    
        