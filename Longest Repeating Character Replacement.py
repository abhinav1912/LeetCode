class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            curr = r-l+1
            if curr - max(count.values()) <= k:
                ans = max(ans, curr)
            else:
                count[s[l]] = count[s[l]] - 1
                l += 1
        return ans
