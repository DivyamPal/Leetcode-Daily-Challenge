class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap=[]
        for i, count in freq.items():
            heapq.heappush(heap, (count, i ))  #insert in heap on the basis of count of elemets
            if len(heap)==k+1:    #if heap len becomes > k so pop the element
                heapq.heappop(heap)
                
        return [ x[1] for x in heap ]
        
