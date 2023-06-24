#This code finds the index of the first occurence in the String.
class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '':
            return 0

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
