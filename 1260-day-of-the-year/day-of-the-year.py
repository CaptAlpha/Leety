class Solution:
    def dayOfYear(self, date: str) -> int:
        
        hashmap = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        def isLeap(year):
            if year%4 == 0:
                if year%100 == 0 and year%400 != 0:
                    return False
                return True
            return False

        def addDays(month, year, days):
            if isLeap(year):
                if month>2:
                    days+=1
            for i in range(1, month):
                days += hashmap[i]
            return days


        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        print(year, month, day)



        return addDays(month, year, day)