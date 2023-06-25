class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1

        distinct_ways = [1, 2]
        for i in range(2, n):
            distinct_ways.append(distinct_ways[i - 1] + distinct_ways[i - 2])
    
        return distinct_ways[n - 1]



        