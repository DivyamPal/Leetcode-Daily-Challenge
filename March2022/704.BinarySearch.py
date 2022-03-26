class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left + right) / 2
            mid = int(mid)
            if nums[mid] == target:
                print(1)
                return mid
            elif nums[mid] < target:
                print(2)
                left = mid+1
            else:
                print(3)
                right = mid-1
        return -1
