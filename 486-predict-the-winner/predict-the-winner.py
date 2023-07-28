class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def canWin(start, end):
            if start == end:
                return nums[start]

            # If Player 1 selects the current number, Player 2 can select from the remaining range
            pick_start = nums[start] - canWin(start + 1, end)

            # If Player 1 selects the last number, Player 2 can select from the remaining range
            pick_end = nums[end] - canWin(start, end - 1)

            # Player 1 chooses the maximum value from both options
            return max(pick_start, pick_end)

        return canWin(0, len(nums) - 1) >= 0
        