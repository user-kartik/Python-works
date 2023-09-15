class Solution(object):
    def lengthOfLastWord(self, s):
            words = s.split()
            if len(words) == 0:
                return 0
            return len(words[-1])
    

       
        