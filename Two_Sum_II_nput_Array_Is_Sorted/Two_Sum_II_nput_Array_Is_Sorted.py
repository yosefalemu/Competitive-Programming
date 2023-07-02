class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftpt = 0
        rightpt = len(numbers) - 1
        ans = []
        while leftpt <= rightpt:
            if numbers[leftpt] + numbers[rightpt] < target:
                leftpt += 1
            elif numbers[leftpt] + numbers[rightpt] > target:
                rightpt -= 1
            else:
                ans.append(leftpt + 1)
                ans.append(rightpt + 1)
                break
        return ans
                
        
