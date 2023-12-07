import heapq
class Solution:
    def spanningTree(self, V, adj):
        pq = [(0, 0)]  # (wt, node)
        vis = [0] * V
        sum = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if vis[node] == 1:
                continue

            vis[node] = 1
            sum += wt

            for neighbor in adj[node]:
                adjNode, edW = neighbor[0], neighbor[1]
                if not vis[adjNode]:
                    heapq.heappush(pq, (edW, adjNode))

        return sum

if __name__ == "__main__":
    V = 5
    edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
    adj = [[] for _ in range(V)]

    for it in edges:
        adj[it[0]].append([it[1], it[2]])
        adj[it[1]].append([it[0], it[2]])

    obj = Solution()
    result = obj.spanningTree(V, adj)
    print("The sum of all the edge weights:", result)