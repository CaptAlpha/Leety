class Solution:
    def numRabbits(self, answers: List[int]) -> int:
         # We are trying to create new groups when a new number is seen
        # If a nuber already exists, then try to fit them in the sam group they were in
        # If the limit is reached then create a new group.
        hashTable = {}
        _id = 0
        
        for i in answers:
            found_group = False
            
            for tableId in list(hashTable.keys()):
                cap, curr = hashTable[tableId]
                if cap == i + 1 and curr < cap:
                    hashTable[tableId] = [cap, curr + 1]
                    found_group = True
                    break
            
            if not found_group:
                _id += 1
                hashTable[_id] = [i + 1, 1]
        
        return sum(cap for cap, curr in hashTable.values())