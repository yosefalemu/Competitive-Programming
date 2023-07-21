class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left,total,count,ans= 0, 0, {}, 0
        for r in range(len(fruits)):
            if fruits[r] in count:
                count[fruits[r]] += 1
            else:
                count[fruits[r]] = 1
            total += 1
            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                total -= 1
                left += 1
            ans = max(ans,total)
        return ans
            
        