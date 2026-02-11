class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        result = []
        
        if not nums:
            return result
        
        start = nums[0]
        
        for i in range(0, len(nums)):
            current_number = nums[i]
            
            # If last element
            if current_number == nums[len(nums) - 1]:
                if start == current_number:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{current_number}")
                break
            
            # If consecutive
            if current_number + 1 == nums[i + 1]:
                continue
            else:
                if start == current_number:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{current_number}")
                
                start = nums[i + 1]
        
        return result


# This code is written completly by me