class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        minTime = 0
        maxTime = max(ranks)*cars*cars

        def check(ranks, cars, mid):
            n = 0
            for i in ranks:
                n += int(math.sqrt((mid/i)))
            #     print(f"Rank {i} can do {} cars in {mid} mins, :: Required cars are {cars}")
            # print(f"Rank {} can do {n} cars in {mid} mins, :: Required cars are {cars}")
            if n >= cars:
                return True
            return False

        while minTime < maxTime:
            mid = (minTime + maxTime) // 2
            if check(ranks, cars, mid):
                maxTime = mid
            else:
                minTime = mid + 1

        return minTime