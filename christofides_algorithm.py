import networkx as nx

def create_complete_graph(distance_matrix):
    num_nodes = len(distance_matrix)
    G = nx.Graph()
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            G.add_edge(i, j, weight=distance_matrix[i][j])
    return G

def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)

def find_odd_degree_nodes(graph):
    odd_degree_nodes = []
    for node in graph.nodes():
        if graph.degree(node) % 2 != 0:
            odd_degree_nodes.append(node)
    return odd_degree_nodes

def minimum_weight_perfect_matching(graph, nodes):
    max_weight_matching = nx.max_weight_matching(graph, weight='weight')
    min_weight_matching = nx.Graph()
    for u, v in max_weight_matching:
        min_weight_matching.add_edge(u, v, weight=graph[u][v]['weight'])
    return min_weight_matching

def combine_graphs(graph1, graph2):
    combined_graph = nx.Graph()
    combined_graph.add_edges_from(graph1.edges(data=True))
    combined_graph.add_edges_from(graph2.edges(data=True))
    return combined_graph

def eulerian_circuit(graph):
    circuit = []
    stack = [list(graph.nodes())[0]] 
    while stack:
        current_node = stack[-1]
        if graph.degree(current_node) == 0:
            circuit.append(stack.pop())
        else:
            next_node = next(graph.neighbors(current_node))
            graph.remove_edge(current_node, next_node) 
            stack.append(next_node)
    return circuit[::-1] 

def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]
    return total_cost


def christofides_tsp(distance_matrix):
    complete_graph = create_complete_graph(distance_matrix)
    min_spanning_tree = minimum_spanning_tree(complete_graph)
    odd_degree_nodes = find_odd_degree_nodes(min_spanning_tree)
    min_weight_matching = minimum_weight_perfect_matching(complete_graph, odd_degree_nodes)
    augmented_graph = combine_graphs(min_spanning_tree, min_weight_matching)
    eulerian_circuit_edges = eulerian_circuit(augmented_graph)
    visited = [False] * len(distance_matrix)
    tour = []

    for node in eulerian_circuit_edges:
        if not visited[node]:
            tour.append(node)
            visited[node] = True

    tour.append(tour[0])

    return tour

'''
minimum_distance = christofides_tsp(distance_matrix)
total_cost = calculate_tour_cost(minimum_distance, distance_matrix)

print("Minimização da distância:", minimum_distance)
print("Custo mínimo: ", total_cost)
'''