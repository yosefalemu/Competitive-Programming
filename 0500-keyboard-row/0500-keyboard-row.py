class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        string1 = "qwertyuiop"
        string2 = "asdfghjkl"
        string3 = "zxcvbnm"
        ans = []
        
        for c in words:
            word = c.lower()
            if len(set(string1 + word)) == len(string1) or len(set(string2 + word)) ==len(string2) or len(set(string3 + word)) == len(string3):
                ans.append(c)
        return ans
                
        