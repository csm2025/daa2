import heapq

iPair = tuple

def addEdge(adj, u, v, w):
    adj[u].append((v, w))
    adj[v].append((u, w))

def shortestPath(adj, V, src):
    pq = []
    heapq.heappush(pq, (0, src))
    dist = [float('inf')] * V
    dist[src] = 0

    while pq:
        d, u = heapq.heappop(pq)

        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    for i in range(V):
        print(f"{i} \t\t {dist[i]}")

if __name__ == "__main__":
    V = 9
    adj = [[] for _ in range(V)]

    addEdge(adj, 0, 1, 4)
    addEdge(adj, 0, 7, 8)
    addEdge(adj, 1, 2, 8)
    addEdge(adj, 1, 7, 11)
    addEdge(adj, 2, 3, 7)
    addEdge(adj, 2, 8, 2)
    addEdge(adj, 2, 5, 4)
    addEdge(adj, 3, 4, 9)
    addEdge(adj, 3, 5, 14)
    addEdge(adj, 4, 5, 10)
    addEdge(adj, 5, 6, 2)
    addEdge(adj, 6, 7, 1)
    addEdge(adj, 6, 8, 6)
    addEdge(adj, 7, 8, 7)

    shortestPath(adj, V, 0)