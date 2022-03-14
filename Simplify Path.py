class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        stack = []
        for i in l:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == ".":
                pass
            elif i:
                stack.append(i)
        if not stack:
            return "/"
        ans = ""
        for i in stack:
            ans += "/"+i
        return ans
