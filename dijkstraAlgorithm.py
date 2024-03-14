def path_vertex(path):
    print( ' ➔ '.join(path))

def min_distance(distances, processed):
    min_distance = float('inf')
    min_index = 0
    
    for vertex in range(len(distances)):
        if distances[vertex] < min_distance and not processed[vertex]:
            min_distance = distances[vertex]
            min_index = vertex
    return min_index

def dijkstra(graph, source, destination):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    processed = [False] * num_vertices
    path = [[] for _ in range(num_vertices)]

    for _ in range(num_vertices):
        current_vertex = min_distance(distances, processed)
        processed[current_vertex] = True
        for neighbor in range(num_vertices):
            if graph[current_vertex][neighbor] > 0 and not processed[neighbor] and distances[neighbor] > distances[current_vertex] + graph[current_vertex][neighbor]:
                distances[neighbor] = distances[current_vertex] + graph[current_vertex][neighbor]
                path[neighbor] = path[current_vertex] + [current_vertex]

    print("\nCusto mínimo:", distances[destination])
    path_vertex([chr(65 + vertex) for vertex in path[destination]] + [chr(65 + destination)])