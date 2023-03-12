class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        intial_length = len(s) % k
        group_text = s[:intial_length]
        for i in range(intial_length,len(s),k):
            if  group_text:
                group_text += "-"
            group_text += s[i: i + k]
        return group_text
                
            
        
                
            