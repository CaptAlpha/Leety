class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        p = 0
        for i in range(len(seats)):
            n = abs(seats[i]-students[i])
            p+=n
        return p
