class Solution(object):
    def longestCommonPrefix(self, str:list[str])->str:
        minimum, maximum = min(str), max(str)
        for i in range(len(minimum)):
            if minimum[i] != maximum[i]:
                return minimum[:i]
        return minimum
                
print(Solution().longestCommonPrefix(["clever", "clumsy", "clue", "cloud"]))
