class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        clean = ''.join([ch.lower() for ch in s if ch.isalnum()])
        e = len(clean)-1

        print(clean)

        while st < e:
            print(f"{st}, {clean[st]}")
            print(f"{e}, {clean[e]}")
            if clean[st] != clean[e]:
                return False
            st += 1
            e -= 1
            
        return True
