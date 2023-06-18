#In this code we are incrementing the large integer by one and return the resulting array of digits.
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        carry = 1  

        for i in range(n - 1, -1, -1):
            digits[i] += carry  
            carry = digits[i] // 10 
            digits[i] %= 10  

        if carry:
            digits.insert(0, carry)

        return digits
