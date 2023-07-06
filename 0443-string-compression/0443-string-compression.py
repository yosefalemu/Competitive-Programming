class Solution:
    def compress(self, chars: List[str]) -> int:
        leftpt = rightpt = i = 0
        n = len(chars)
        while leftpt < len(chars):
            if n !=rightpt and chars[leftpt] == chars[rightpt]:
                rightpt += 1
            else:
                chars[i] = chars[leftpt]
                i += 1
                val = rightpt - leftpt
                if val > 1:
                    for c in str(val):
                        chars[i] = c
                        i += 1
                leftpt = rightpt
        return i
        
        