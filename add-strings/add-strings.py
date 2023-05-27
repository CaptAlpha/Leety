class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        carry = 0
        result = ""

        # Iterate from right to left
        i = n1 - 1
        j = n2 - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0

            digit2 = int(num2[j]) if j >= 0 else 0

            digit_sum = digit1 + digit2 + carry
            carry = digit_sum // 10  # Update the carry
            digit_sum %= 10  # Calculate the current digit

            result = str(digit_sum) + result

            i -= 1
            j -= 1

        return result
