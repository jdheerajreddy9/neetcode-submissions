class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = "".join(char.lower() for char in s if char.isalnum())
        rev = final[::-1]
        if rev == final:
            return True
        else:
            return False
        