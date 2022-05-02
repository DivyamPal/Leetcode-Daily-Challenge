class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        index=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i],nums[index]=nums[index],nums[i]
                index+=1
        print(nums)
        return nums
