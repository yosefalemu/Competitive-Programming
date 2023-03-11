class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            divisibleb_by_3 = (i % 3 == 0)
            divisibleb_by_5 = (i % 5 == 0)
            if divisibleb_by_3 and divisibleb_by_5:
                ans.append("FizzBuzz")
            elif divisibleb_by_3:
                ans.append("Fizz")
            elif divisibleb_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans