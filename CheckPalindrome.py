class Solution(object):
    def checkPalindrome(self, arr):
        n = len(arr)
        l, r = 0, n-1
        while l <= r:
            if arr[l] == arr[r]:
                l+=1
                r-=1
                return True
            else:
                return False
print(Solution().checkPalindrome("abcdedcba"))
