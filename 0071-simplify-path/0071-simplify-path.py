class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = []
        temp = ""
        for c in path + "/":
            if c == "/":
                if arr and temp == "..":
                    arr.pop()
                elif temp == "..":
                    pass
                elif temp and temp != ".":
                    arr.append(temp)
                else:
                    pass
                temp = ""
            else:
                temp += c
        return "/" + "/".join(arr)
                        
                
            
        