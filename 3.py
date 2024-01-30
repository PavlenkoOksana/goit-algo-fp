import heapq

def dijkstra(graph, start_vertex):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start_vertex] = 0

    priority_queue = [(0, start_vertex)]
 
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distance[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            new_distance = distance[current_vertex] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distance

# Приклад використання:
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 7)],
    "C": [("D", 1)],
    "D": []
}

start_vertex = "A"
shortest_distances = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in shortest_distances.items():
    print(f"{vertex}: {distance}")