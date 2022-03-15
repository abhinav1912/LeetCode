class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        ans = ""
        stack = []
        for i in s:
            if i=="(":
                count += 1
                stack.append(i)
            elif i == ")":
                count -= 1
                if count < 0:
                    count = 0
                else:
                    stack.append(i)
            else:
                stack.append(i)
        while stack:
            t = stack.pop()
            if t == "(":
                if count:
                    count -=1
                else:
                    ans += t
            elif t == ")":
                ans += t
            else:
                ans += t
        return ans[::-1]
