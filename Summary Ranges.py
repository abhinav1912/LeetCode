class Solution:
    def summaryRanges(self, l: List[int]) -> List[str]:
        if not l:
            return []
        if len(l) == 1:
            return [str(l[0])]
        ranges = []
        curr = [l[0], l[0]]
        for i in range(1,len(l)):
            if l[i] == curr[1]+1:
                curr[1] = l[i]
            else:
                ranges.append(curr)
                curr = [l[i], l[i]]
        ranges.append(curr)
        ans = []
        for i in ranges:
            if i[0] == i[1]:
                ans.append(str(i[0]))
            else:
                ans.append(f"{i[0]}->{i[1]}")
        return ans
