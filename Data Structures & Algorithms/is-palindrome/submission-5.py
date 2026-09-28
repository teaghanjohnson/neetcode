class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1

        mid = (l + r) / 2
        if len(s) == 1:
            return True

        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            elif not s[l].isalnum():
                l += 1
            else:
                r -= 1 
        
        return True