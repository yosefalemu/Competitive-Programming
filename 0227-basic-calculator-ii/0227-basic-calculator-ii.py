class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        opr = "+"
        for c in s + "+":
            if c == " ":
                continue
            elif c.isdigit():
                curr = (curr * 10) + int(c)
            else:
                if opr == "+":
                    stack.append(curr)
                elif opr == "-":
                    stack.append(-curr)
                elif opr == "*":
                    stack.append(stack.pop() * curr)
                elif opr == "/":
                    stack.append(int(stack.pop() / curr))
                curr = 0
                opr = c
        return sum(stack)
                    
                
                
        
                
            
            
        
                 
                
    
                
                
                
        