class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, ans = len(s), 1
        x= s[0]
        for i in range(n-1):
            l,r = i-1, i+1
            while l>=0 and r < n and (s[l] == s[r]):
                if r-l+1 > ans:
                    ans = r-l+1
                    x = s[l:r+1]
                r += 1
                l -= 1
            l,r = i, i+1
            while l>=0 and r < n and (s[l] == s[r]):
                if r-l+1 > ans:
                    ans = r-l+1
                    x = s[l:r+1]
                r += 1
                l -= 1
        return x
