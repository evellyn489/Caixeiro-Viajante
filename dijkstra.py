def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    visited = [False] * num_vertices
    shortest_paths = [[] for _ in range(num_vertices)]  # Lista para armazenar os caminhos mínimos

    for _ in range(num_vertices):
        min_distance = float('inf')
        min_index = -1
        for v in range(num_vertices):
            if distances[v] < min_distance and not visited[v]:
                min_distance = distances[v]
                min_index = v
        
        visited[min_index] = True
        
        for v in range(num_vertices):
            if graph[min_index][v] > 0 and not visited[v] and distances[v] > distances[min_index] + graph[min_index][v]:
                distances[v] = distances[min_index] + graph[min_index][v]
                shortest_paths[v] = shortest_paths[min_index] + [min_index]  # Atualiza o caminho mínimo até o vértice v
    
    return distances, shortest_paths


def nearest_neighbor(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    path = [start]
    visited[start] = True
    
    current_vertex = start
    
    while len(path) < num_vertices:
        next_vertex = None
        min_distance = float('inf')
        
        for v in range(num_vertices):
            if not visited[v] and graph[current_vertex][v] > 0 and graph[current_vertex][v] < min_distance:
                next_vertex = v
                min_distance = graph[current_vertex][v]
        
        if next_vertex is not None:
            path.append(next_vertex)
            visited[next_vertex] = True
            current_vertex = next_vertex
        else:
            break
    
    path.append(start)  # Adiciona o vértice inicial para completar o ciclo
    
    return path

def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    return cost - graph[path[-1]][path[0]]  # Exclui a última aresta do custo total

