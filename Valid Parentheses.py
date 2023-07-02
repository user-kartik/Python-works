class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    
        for char in s:
            if char in bracket_pairs:
                stack.append(char)
            elif char in bracket_pairs.values():
                if not stack or bracket_pairs[stack.pop()] != char:
                    return False
    
        return len(stack) == 0