class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_prefix = 0
        max_prefix = 0
        
        for d in differences:
            prefix += d
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)
        
        # Calculate the lower and upper bounds for the starting value s
        lower_bound = max(lower, lower - min_prefix)
        upper_bound = min(upper, upper - max_prefix)
        
        if upper_bound < lower_bound:
            return 0
        return upper_bound - lower_bound + 1