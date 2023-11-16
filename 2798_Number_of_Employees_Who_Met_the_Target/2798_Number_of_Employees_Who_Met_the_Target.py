class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for c in hours:
            if c >= target:
                count += 1
        return count
