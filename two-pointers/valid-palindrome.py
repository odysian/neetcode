class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean string of spaces and non alphanum chars
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        # Two pointers, one at each end
        left = 0
        right = len(cleaned) - 1

        while left < right:
            # Compare
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
