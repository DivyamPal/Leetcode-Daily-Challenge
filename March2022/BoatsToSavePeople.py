class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat,left,right=0,0,len(people)-1
        while left<=right:
            res=people[left]+people[right]
            if res<=limit:
                left+=1
                right-=1
                boat+=1
            if res>limit:
                right-=1
                boat+=1
        return boat
