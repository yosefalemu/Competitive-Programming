class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        leftpt = rightpt = 0
        while leftpt < len(word1) and rightpt < len(word2):
            if word1[leftpt] > word2[rightpt]:
                merge.append(word1[leftpt])
                leftpt += 1
            elif word1[leftpt] < word2[rightpt]:
                merge.append(word2[rightpt])
                rightpt += 1
            else:
                if word1[leftpt:] > word2[rightpt:]:
                    merge.append(word1[leftpt])
                    leftpt += 1
                else:
                    merge.append(word2[rightpt])
                    rightpt += 1
        while leftpt < len(word1):
            merge.append(word1[leftpt])
            leftpt += 1
        while rightpt < len(word2):
            merge.append(word2[rightpt])
            rightpt += 1
        return "".join(merge)