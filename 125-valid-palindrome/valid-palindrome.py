class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (cleaned := ''.join(char.lower() for char in s if char.isalnum())) == cleaned[::-1]
