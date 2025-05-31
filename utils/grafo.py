import heapq

def build_graph(distancias):
    graph = {}
    for (u, v), (dist, dur) in distancias.items():
        if u not in graph:
            graph[u] = []
        graph[u].append((v, dist, dur))
    return graph

def dijkstra(graph, start, end):
    heap = [(0, 0, start, [])]
    visited = set()

    while heap:
        current_distance, current_duration, current_node, path = heapq.heappop(heap)
        if current_node == end:
            return current_distance, current_duration, path
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, dist, dur in graph.get(current_node, []):
            if neighbor in visited:
                continue
            new_distance = current_distance + dist
            new_duration = current_duration + dur
            new_path = path + [(current_node, neighbor, dist, dur)]
            heapq.heappush(heap, (new_distance, new_duration, neighbor, new_path))
    return None, None, None
