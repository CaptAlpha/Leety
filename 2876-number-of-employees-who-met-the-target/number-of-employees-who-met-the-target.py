class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = len(hours)
        for i in hours: 
            if i < target: count-=1
        return count

        