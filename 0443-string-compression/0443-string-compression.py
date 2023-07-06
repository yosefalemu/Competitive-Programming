class Solution:
    def compress(self, chars: List[str]) -> int:
        leftpt = rightpt = i = 0
        n = len(chars)
        while leftpt < n:
            while rightpt < n and chars[rightpt] == chars[leftpt]:
                rightpt += 1
            chars[i] = chars[leftpt]
            i += 1
            if rightpt - leftpt > 1:
                for c in str(rightpt - leftpt):
                    chars[i] = c
                    i += 1
            leftpt = rightpt
        return i
        
        