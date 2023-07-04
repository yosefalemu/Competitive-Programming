class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = i
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, dict[s[i]])
            if i == end:
                output.append(end - start + 1)
                start = end + 1
        return output
