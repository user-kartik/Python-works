class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        total = 0
        prev_value = 0

        for i in range(len(s) - 1, -1, -1):
            curr_value = roman_dict[s[i]]
        
            if curr_value >= prev_value:
                total += curr_value
            else:
                total -= curr_value

            prev_value = curr_value
        return total