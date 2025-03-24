class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        meetings.sort()
        merged = [meetings[0]]
        
        for s, e in meetings[1:]:
            last_s, last_e = merged[-1]
            if s <= last_e + 1:
                merged[-1] = (last_s, max(last_e, e))
            else:
                merged.append((s, e))
        
        covered = sum(e - s + 1 for s, e in merged)
        return days - covered