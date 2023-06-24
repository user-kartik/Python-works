class Solution(object):
    def longestArithSeqLength(self, nums):
        n = len(nums)
        if n <= 2:
            return n

        dp = [{} for _ in range(n)]

        max_length = 2  

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                length = dp[j].get(diff, 1) + 1

                max_length = max(max_length, length)

                dp[i][diff] = length

        return max_length
