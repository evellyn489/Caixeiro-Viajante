def min_distance(distances, processed):
    min_distance = float('inf')
    min_index = 0
    
    for vertex in range(len(distances)):
        if distances[vertex] < min_distance and not processed[vertex]:
            min_distance = distances[vertex]
            min_index = vertex
    return min_index

def dijkstra_pcv(graph, source):
    num_vertices = len(graph)
    distances = [[float('inf')] * num_vertices for _ in range(1 << num_vertices)]
    distances[1 << source][source] = 0
    parent = [[-1] * num_vertices for _ in range(1 << num_vertices)]

    for mask in range(1, 1 << num_vertices):
        for current_vertex in range(num_vertices):
            if not (mask & (1 << current_vertex)):
                continue
            for neighbor in range(num_vertices):
                if mask & (1 << neighbor):
                    continue
                next_mask = mask | (1 << neighbor)
                if distances[mask][current_vertex] + graph[current_vertex][neighbor] < distances[next_mask][neighbor]:
                    distances[next_mask][neighbor] = distances[mask][current_vertex] + graph[current_vertex][neighbor]
                    parent[next_mask][neighbor] = current_vertex

    # Encontra o vértice de origem no caminho mínimo
    mask = (1 << num_vertices) - 1
    min_cost = min(distances[mask][v] + graph[v][source] for v in range(num_vertices))
    min_vertex = min(range(num_vertices), key=lambda v: distances[mask][v] + graph[v][source])

    # Reconstrói o caminho mínimo
    path = []
    while min_vertex != -1:
        path.append(min_vertex)
        mask ^= 1 << min_vertex
        min_vertex = parent[mask][min_vertex]

    # Inverte a ordem dos vértices no caminho mínimo para que a ordem comece do vértice de origem
    path.reverse()

    # Verifica se todos os vértices foram visitados no caminho mínimo
    visited = set(path)
    for vertex in range(num_vertices):
        if vertex not in visited:
            path.append(vertex)

    # Retorna o caminho mínimo e o custo mínimo
    return path, min_cost
