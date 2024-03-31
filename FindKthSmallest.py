def KthSmallest(self, arr, k):
        heapq.heapify(arr)
        for i in range(k):
            result = heapq.heappop(arr)
        return result
            
print(Solution().KthSmallest([5, 2, 10, 14, 3, 9], 4))

