# 14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i+= 1
            prefix = prefix[:i]

            if prefix == "":
                break

        
        return prefix
    