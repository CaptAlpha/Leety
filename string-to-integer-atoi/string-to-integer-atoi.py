class Solution(object):
    def myAtoi(self, s):
        r = "0123456789"
        res = ""
        sign = 1
        i = 0

        # Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        # Check for a sign
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Append numeric characters
        while i < len(s) and s[i] in r:
            res += s[i]
            i += 1

        # Handle overflow
        try:
            ans = int(res) * sign
            return max(min(ans, 2**31 - 1), -2**31)
        except ValueError:
            return 0
