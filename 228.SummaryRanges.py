class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result=[]
        start=0
        if nums==[] or len(nums)==1:
            return list(map(str,nums))
        for i in range(len(nums)):
            if i==len(nums)-1 or nums[i+1]!=nums[i]+1:
                if nums[start]==nums[i]:
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[start])+"->"+str(nums[i]))
                start=i+1
        return result
