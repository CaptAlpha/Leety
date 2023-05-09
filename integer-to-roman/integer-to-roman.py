class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        result = ''
        # Iterate over the dictionary keys in descending order
        for val in sorted(dic.keys(), reverse=True):
        
            while num >= val:
                num -= val
                result += dic[val]
        # Return the resulting Roman numeral string
        return result
            
            

        