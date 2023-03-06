class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = -1
        while i >= -1 * len(s):
            if s[i] != " ":
                j = i
                while j >= -1 * len(s):
                    if s[j] != " ":
                        count += 1
                        j -= 1
                    else:
                        break
                break
            i -= 1
        return count
                
                
                
              