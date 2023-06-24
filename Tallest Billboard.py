class Solution(object):
    def tallestBillboard(self, rods):
        dp = {0: 0}
    
        for rod in rods:
            curr_dp = dp.copy()
        
            for length, height in curr_dp.items():
                dp[length + rod] = max(dp.get(length + rod, 0), height)
                dp[abs(length - rod)] = max(dp.get(abs(length - rod), 0), height + min(length, rod))
    
        return dp.get(0, 0)
