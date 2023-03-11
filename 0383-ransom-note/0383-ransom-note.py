class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1, counter2 = Counter(ransomNote), Counter(magazine)
        return not counter1 - counter2
            
            
        