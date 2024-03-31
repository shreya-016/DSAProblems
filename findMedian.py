class Solution(object):
    def findMedian(self, arr):
        n = len(arr)
        l, r = 0, n-1
        while l <= r:
            mid = l + (r-l) // 2
            if n%2 == 0:
                return (mid + (mid+1))//2
            else:
                return mid // 2
                
print(Solution().findMedian([2, 3, 4, 7, 8, 10, 13, 14]))
