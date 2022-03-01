class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,ans,n = 0,0,len(s)
        d = {}
        for r in range(n):
            if s[r] not in d:
                ans = max(ans, r-l+1)
            else:
                if d[s[r]] >= l:
                    l = d[s[r]] + 1
                else:
                    ans = max(ans, r-l+1)
            d[s[r]] = r
        return ans
