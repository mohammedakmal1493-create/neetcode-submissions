class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1

        while i < j:

            if not s[i].lower().isalnum():
                i += 1
                continue

            if not s[j].lower().isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True