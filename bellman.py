def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

# Example usage
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'C': -1, 'D': 1},
    'C': {'B': 3, 'D': 2},
    'D': {'C': -3}
}

start_node = 'A'
distances = bellman_ford(graph, start_node)

print(distances)
