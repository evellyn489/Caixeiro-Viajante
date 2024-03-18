class Dijkstra:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.quantity_cities = len(graph)
    
    def solve(self):
        path = [self.start_vertex]
        visited_cities = {self.start_vertex}
        current_city = self.start_vertex
        total_distance = 0
        
        while len(visited_cities) < self.quantity_cities:
            nearest_distance = float('inf')
            nearest_neighbor = None
            
            for neighbor in range(self.quantity_cities):
                if neighbor not in visited_cities:
                    distance = self.graph[current_city][neighbor]
                    if distance < nearest_distance:
                        nearest_neighbor = neighbor
                        nearest_distance = distance

            if nearest_neighbor is not None:
                path.append(nearest_neighbor)
                visited_cities.add(nearest_neighbor)
                current_city = nearest_neighbor
                total_distance += nearest_distance
            else:
                break
        
        total_distance += self.graph[path[-1]][self.start_vertex]
        path.append(self.start_vertex)
        
        return path, total_distance


graph = [
    [0, 3, 4, 2, 7],
    [3, 0, 4, 6, 3],
    [4, 4, 0, 5, 8],
    [2, 6, 5, 0, 6],
    [7, 3, 8, 6, 0]
]


# Vértice de partida
start_vertex = 0

tsp_solver = Dijkstra(graph, start_vertex)
tsp_path, tsp_distance = tsp_solver.solve()
print("Caminho encontrado pelo algoritmo de Dijkstra para o TSP:", tsp_path)
print("Comprimento total do caminho:", tsp_distance)