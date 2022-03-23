class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        steps = 0
        while x<y:
            steps += (y%2) + 1
            y = (y+1)//2
        return steps + (x-y)
