class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        df = {}
        for n in nums:
            if n in df:
                df[n] += 1
            else:
                df[n] = 1
        l = len(nums)/2
        for x in df:
            if df[x] > l:
                return x
        