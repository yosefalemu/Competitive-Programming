class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right, turn):
            if left > right:
                return 0
            if turn:
                # If it's the current player's turn, they will choose the maximum score
                score_by_left = nums[left] + helper(left + 1, right, not turn)
                score_by_right = nums[right] + helper(left, right - 1, not turn)
                return max(score_by_left, score_by_right)
            else:
                # If it's the opponent's turn, they will choose the minimum score
                score_by_left = -nums[left] + helper(left + 1, right, not turn)
                score_by_right = -nums[right] + helper(left, right - 1, not turn)
                return min(score_by_left, score_by_right)
        
        return helper(0, len(nums) - 1, True) >= 0
