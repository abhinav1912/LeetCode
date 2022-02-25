class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        v = len(v1)-len(v2)
        if v>0:
            v2 += [0]*v
        elif v<0:
            v1 += [0]*(v*-1)
        if v1==v2:
            return 0
        if v1>v2:
            return 1
        return -1
