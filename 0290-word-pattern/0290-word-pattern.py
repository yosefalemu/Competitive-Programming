class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        letterdic = {}
        worddic = {}
        for letter, word in zip(pattern, word):
            if letter not in letterdic:
                letterdic[letter] = word
            elif letterdic[letter] != word:
                return False
            if word not in worddic:
                worddic[word] = letter
            elif worddic[word] != letter:
                return False
        return True