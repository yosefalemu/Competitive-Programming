class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string1 = ""
        for i in range(len(digits)):
            string1 += str(digits[i])
        number = int(string1) + 1
        string1 = str(number)
        ans = []
        for i in string1:
            ans.append(int(i))
        return ans
