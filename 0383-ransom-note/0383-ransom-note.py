class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        dict2 = {}
        for c in ransomNote:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        for c in magazine:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1
        for c in dict1:
            if c not in dict2 or dict1[c] > dict2[c]:
                return False
        return True
            
            
        