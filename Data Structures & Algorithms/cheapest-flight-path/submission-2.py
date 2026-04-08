class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[inf]*(k +5) for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])
        
        dist[src][0] = 0
        minHead = [(0, src, -1)]

        while len(minHead):
            cst , node ,stops = heapq.heappop(minHead)
            if dst == node: return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue
            
            for nei ,w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[nei][nextStops +1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHead, (nextCst, nei, nextStops))
        return -1