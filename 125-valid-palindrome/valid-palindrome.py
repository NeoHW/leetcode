class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower().replace(" ", "")
        new_s = ''.join(char for char in new_s if char.isalnum())
        n = len(new_s)
        left, right = 0, n-1
        while left <= right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        
        return True