import networkx as nx
import matplotlib.pyplot as plt
from unionfind import unionfind


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



# def adjacency_matrix_to_weighted_graph_from_file(filename):
#     weighted_graph = {}

#     with open(filename, 'r') as file:
#         lines = file.readlines()
#         num_nodes = len(lines)

#         for i in range(num_nodes):
#             node_name = str(i)  # Converte o índice para a letra maiúscula correspondente
#             weighted_graph[node_name] = []

#             values = lines[i].split()
#             for j in range(num_nodes):
#                 weight = int(values[j])
#                 if weight != 0:  # Apenas adiciona arestas com peso diferente de zero
#                     dest_name = str(j)  # Converte o índice para a letra maiúscula correspondente
#                     weighted_graph[node_name].append((weight, dest_name, node_name))

#     return weighted_graph

# def draw_weighted_graph(weighted_graph):
#     G = nx.Graph()

#     for node, edges in weighted_graph.items():
#         for weight, dest, src in edges:
#             G.add_edge(src, dest, weight=weight)

#     pos = nx.spring_layout(G)
#     labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw(G, pos, with_labels=True)
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#     plt.show()

# # Nome do arquivo contendo a matriz de adjacência
# filename = "datasets/five.txt"

# # Converter matriz de adjacência para grafo ponderado
# weighted_graph = adjacency_matrix_to_weighted_graph_from_file(filename)

# # Exibir grafo ponderado
# draw_weighted_graph(weighted_graph)






# from unionfind import unionfind

# def load_graph_from_file(filename):
#     graph = {}
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.split()
#             node1, node2, cost = parts[0], parts[1], int(parts[2])
#             if node1 not in graph:
#                 graph[node1] = []
#             if node2 not in graph:
#                 graph[node2] = []
#             graph[node1].append((cost, node1, node2))
#             graph[node2].append((cost, node2, node1))
#     return graph

# def load_edges(G):
#     num_nodes = 0
#     edges = []

#     for _, value in G.items(): 
#         num_nodes += 1
#         edges.extend(value)

#     return num_nodes, sorted(edges)

# def conv_char(c):
#     return ord(c) - 65

# def kruskals(G):
#     total_cost = 0
#     MST = []

#     num_nodes, edges = load_edges(G)
#     uf = unionfind(num_nodes)

#     for edge in edges:
#         cost, n1, n2 = edge[0], edge[1], edge[2]

#         if not uf.issame(conv_char(n1), conv_char(n2)):
#             total_cost += cost
#             uf.unite(conv_char(n1), conv_char(n2))
#             MST.append((n1, n2, cost))

#     return MST, total_cost

# def main():
#     # Substitua 'seu_arquivo.txt' pelo caminho do seu arquivo de dados
#     graph_file = "datasets/att48.txt"
#     G = load_graph_from_file(graph_file)
#     MST, total_cost = kruskals(G)

#     print(f'Minimum spanning tree: {MST}')
#     print(f'Total cost: {total_cost}')

# main()