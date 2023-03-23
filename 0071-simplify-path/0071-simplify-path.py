class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = []
        temp = ""
        for c in path + "/":
            if c == "/":
                if temp == "..":
                    if arr:
                        arr.pop()
                elif temp and temp != ".":
                    arr.append(temp)
                else:
                    pass
                temp = ""
            else:
                temp += c
        return "/" + "/".join(arr)
                        
                
            
        