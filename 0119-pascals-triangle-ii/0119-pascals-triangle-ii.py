class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        if rowIndex == 0:
            return ans
        else:
            for i in range(rowIndex):
                temp = [0] + ans + [0]
                ans = []
                for j in range(len(temp) - 1):
                    ans.append(temp[j] + temp[j + 1])
        return ans