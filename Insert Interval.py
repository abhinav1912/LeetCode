class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        for i in range(len(intervals)):
            val = intervals[i]
            if val[1] < newInterval[0]:
                ans.append(val)
            elif val[0] > newInterval[1]:
                ans = ans + [newInterval] + intervals[i:]
                return ans
            else:
                newInterval[0] = min(newInterval[0], val[0])
                newInterval[1] = max(newInterval[1], val[1])
        ans.append(newInterval)
        return ans
