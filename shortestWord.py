class Solution():
    def shortestWord(self, arr):
        shortestWord = arr[0]
        for word in arr[1:]:
            if len(word) < len(shortestWord):
                shortestWord = word
                
        return shortestWord
        
print(Solution().shortestWord(["BlockChain", "Development", "Intern"]))
