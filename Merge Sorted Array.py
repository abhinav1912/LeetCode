class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if a[i] > b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1
            k -= 1
        a[:j+1] = b[:j+1]
