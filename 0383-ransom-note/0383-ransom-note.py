class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1, counter2 = Counter(ransomNote), Counter(magazine)
        if counter1 & counter2 == counter1:
            return True
        else:
            return False
            
            
        