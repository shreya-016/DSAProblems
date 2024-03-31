class Solution(object):
    def FirstOccurance(self, arr, target):
        n = len(arr)
        l, r = 0, n-1
        leftIdx = -1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                leftIdx = mid
                r = mid-1
            elif arr[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return leftIdx
        
print(Solution().FirstOccurance([2, 4, 4, 4, 5, 6, 8,], 4))
