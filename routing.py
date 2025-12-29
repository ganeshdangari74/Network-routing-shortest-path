import sys

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2, 'E': 1},
    'E': {'D': 1}
}

def dijkstra(graph, source):
    distances = {node: sys.maxsize for node in graph}
    distances[source] = 0
    visited = set()

    while len(visited) < len(graph):
        current = min(
            (node for node in distances if node not in visited),
            key=lambda node: distances[node]
        )

        visited.add(current)

        for neighbor, cost in graph[current].items():
            new_distance = distances[current] + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

source_node = 'A'
print("Network Nodes:", list(graph.keys()))
print(f"\nRouting from Source Node: {source_node}\n")

shortest_paths = dijkstra(graph, source_node)

for node, cost in shortest_paths.items():
    print(f"Shortest path cost from {source_node} to {node}: {cost}")