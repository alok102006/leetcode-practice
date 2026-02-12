class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[len(nums)-1]
        else:
            return nums[len(nums)-3]