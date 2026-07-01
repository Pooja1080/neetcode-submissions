class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join([ch.lower() for ch in s if ('a' <= ch <='z') or ('A'<= ch <= 'Z') or ('0' <= ch <= '9')])
        st = 0
        e = len(clean) - 1

        while st < e:
            if clean[st] != clean[e]:
                return False

            st += 1
            e -= 1

        return True
