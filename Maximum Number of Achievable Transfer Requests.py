class Solution(object):
    def maximumRequests(self, n, requests):
        max_requests = 0
    
        for mask in range(1 << len(requests)):
            count = [0] * n 
        
            for i, (fromi, toi) in enumerate(requests):
                if (mask >> i) & 1:
                    count[fromi] -= 1  
                    count[toi] += 1    
        
            if all(x == 0 for x in count):
                max_requests = max(max_requests, bin(mask).count('1'))  
        
        return max_requests