class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score, level = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                level += 1
            else:
                level -=1
                if s[i-1] == "(":
                    score += 1<<level
        return score
