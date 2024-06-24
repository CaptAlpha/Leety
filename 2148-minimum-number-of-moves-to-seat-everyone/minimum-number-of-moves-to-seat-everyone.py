class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        s = 0
        for i in range(len(seats)):
            s+=abs(students[i]- seats[i])
        return s