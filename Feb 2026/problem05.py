
# Solution By me
# num1 = [4,1,2]
# num2 = [1,3,4,2]
# a ={}
# i = 0
# for n in num2:    
#     if n not in a:
#         a[n] = i
#         i += 1
# result = []
# for n in num1:
#     if a[n] == len(num2)-1:
#         result.append(-1)
#     elif num2[(a[n])] < num2[(a[n]+1)]:
#         result.append(num2[(a[n]+1)])
#     else:
#         result.append(-1)
# print(result)

# Solution by chatgpt using stack
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

        