class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        count=0
        for i in range(0, len(costs)):
            if i<len(costs)/2 :
                count+=costs[i][0]
            else:
                count+=costs[i][1]
        return count
