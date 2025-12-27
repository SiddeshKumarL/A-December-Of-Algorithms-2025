from collections import defaultdict
import heapq
import sys

INF = float('inf')

def min_weight_cycle(V, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    min_cycle = INF
    
    for u, v, edge_weight in edges:
        # Dijkstra from u to v excluding direct edge (u,v)
        dist = [INF] * V
        dist[u] = 0
        visited = [False] * V
        pq = [(0, u)]
        
        while pq:
            d, node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            
            for nei, w in graph[node]:
                # Skip the direct edge we're excluding
                if (node == u and nei == v) or (node == v and nei == u):
                    continue
                
                if dist[nei] > d + w:
                    dist[nei] = d + w
                    heapq.heappush(pq, (dist[nei], nei))
        
        if dist[v] != INF:
            cycle_weight = dist[v] + edge_weight
            min_cycle = min(min_cycle, cycle_weight)
    
    return min_cycle if min_cycle != INF else -1

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    V = int(data[index])
    index += 1
    
    edges = []
    # Read edges until end of input (3 numbers per edge)
    while index + 2 < len(data):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        edges.append([u, v, w])
        index += 3
    
    result = min_weight_cycle(V, edges)
    print(result)

if __name__ == "__main__":
    main()
