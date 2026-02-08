class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []

        # Step 1: Process nums2
        for n in nums2:
            while stack and n > stack[-1]:
                next_greater[stack.pop()] = n
            stack.append(n)

        # Step 2: Remaining elements have no next greater
        while stack:
            next_greater[stack.pop()] = -1

        # Step 3: Build result for nums1
        return [next_greater[n] for n in nums1]
