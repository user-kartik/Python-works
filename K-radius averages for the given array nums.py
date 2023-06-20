class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        avgs = [-1] * n
    
        total = 0
        count = 0
    
        for i in range(min(k + 1, n)):
            total += nums[i]
            count += 1
    
        for i in range(n):
            if count >= 2 * k + 1:
                avgs[i] = total // count
        
            if i - k >= 0:
                total -= nums[i - k]
                count -= 1
        
            if i + k + 1 < n:
                total += nums[i + k + 1]
                count += 1
    
        return avgs

        