class Solution(object):
    def addBinary(self, a, b):
        sum_decimal = int(a, 2) + int(b, 2)
        
        return bin(sum_decimal)[2:]





