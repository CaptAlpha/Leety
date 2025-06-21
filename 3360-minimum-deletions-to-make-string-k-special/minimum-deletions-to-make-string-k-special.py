class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        
        freq = Counter(word)
        freq_values = list(freq.values())
        unique_freq = sorted(set(freq_values))
        
        mini = float('inf')
        for target in unique_freq:
            count = 0
            for f in freq_values:
                if f > target + k:
                    count += f - (target + k)
                elif f < target:
                    count += f
            mini = min(mini, count)
        
        return mini
