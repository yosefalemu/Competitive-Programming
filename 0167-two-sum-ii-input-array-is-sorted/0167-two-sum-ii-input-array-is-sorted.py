class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftpt, rightpt = 0, len(numbers) - 1
        while leftpt < rightpt:
            if numbers[leftpt] + numbers[rightpt] == target:
                return list((leftpt + 1, rightpt + 1))
            else:
                if numbers[leftpt] + numbers[rightpt] > target:
                    rightpt -= 1
                else:
                    leftpt += 1
        
        