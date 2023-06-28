import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))
    
        prob = [0.0] * n
        prob[start] = 1.0
    
        pq = [(-1.0, start)]  
        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob  
            if node == end:
                return curr_prob
        
            if curr_prob < prob[node]:
                continue
        
            for neighbor, p in graph[node]:
                new_prob = curr_prob * p
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
    
        return 0.0