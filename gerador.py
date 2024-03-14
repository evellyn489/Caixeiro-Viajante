import networkx as nx
import matplotlib.pyplot as plt

def adjacency_matrix_to_weighted_graph_from_file(filename):
    weighted_graph = {}

    with open(filename, 'r') as file:
        lines = file.readlines()
        num_nodes = len(lines)

        for i in range(num_nodes):
            node_name = str(i)  # Converte o índice para a letra maiúscula correspondente
            weighted_graph[node_name] = []

            values = lines[i].split()
            for j in range(num_nodes):
                weight = int(values[j])
                if weight != 0:  # Apenas adiciona arestas com peso diferente de zero
                    dest_name = str(j)  # Converte o índice para a letra maiúscula correspondente
                    weighted_graph[node_name].append((weight, dest_name, node_name))

    return weighted_graph

def draw_weighted_graph(weighted_graph):
    G = nx.Graph()

    for node, edges in weighted_graph.items():
        for weight, dest, src in edges:
            G.add_edge(src, dest, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Nome do arquivo contendo a matriz de adjacência
filename = "datasets/five.txt"

# Converter matriz de adjacência para grafo ponderado
weighted_graph = adjacency_matrix_to_weighted_graph_from_file(filename)

# Exibir grafo ponderado
draw_weighted_graph(weighted_graph)
