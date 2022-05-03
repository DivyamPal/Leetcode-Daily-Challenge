class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        end=0
        prev=nums[0]
        for i in range(len(nums)):
            if prev<=nums[i]:
                prev=nums[i]
            else:
                end=i
        start=0
        prev=nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            if prev>=nums[i]:
                prev=nums[i]
            else:
                start=i
        if end!=0:
            return end-start+1
        else:
            return 0
    
