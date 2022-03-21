from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter()
        for i,j in enumerate(s):
            count[j] = i
        output = []
        right, left = count[s[0]], 0
        for i, j in enumerate(s):
            right = max(right, count[j])
            if i == right:
                output.append(right-left+1)
                left = i + 1
                right = -1
        return output
