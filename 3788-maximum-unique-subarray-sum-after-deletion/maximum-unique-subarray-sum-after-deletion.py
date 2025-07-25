class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sic = set()
        count, mele = 0, float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                sic.add(nums[i])
            mele = max(mele, nums[i])
        for x in sic:
            count += x
        print(count)
        if len(sic) == 0:
            return mele
        else:
            return count