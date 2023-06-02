class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1
        remaining_capacity = capacity
        current_position = -1
        
        for i in range(len(plants)-1):
            remaining_capacity -= plants[i]

            if remaining_capacity < plants[i+1]:
                steps += ((i+1)*2)+1
                remaining_capacity = capacity

            else:
                steps+=1

        return steps

            