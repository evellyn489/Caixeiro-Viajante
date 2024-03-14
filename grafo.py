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

def plot_weighted_graph_from_dataset(dataset):
    name_file = ""
    if dataset == 1:
        name_file = "./datasets/att48.txt"
    elif dataset == 2:
        name_file = "./datasets/dantzig42.txt"
    elif dataset == 3:
        name_file = "./datasets/fri26.txt"
    elif dataset == 4:
        name_file = "./datasets/gr17.txt"
    elif dataset == 5:
        name_file = "./datasets/p01.txt"
    else:
        print("Não existe essa opção. Selecione um número entre 1 e 5.")
        return

    # Converter matriz de adjacência para grafo ponderado
    weighted_graph = adjacency_matrix_to_weighted_graph_from_file(name_file)

    # Exibir grafo ponderado
    draw_weighted_graph(weighted_graph)

while True:
    print('''\n
        1 - att48
        2 - dantzig42
        3 - fri26
        4 - gr17
        5 - p01
        Escolha qual base de dados quer selecionar ou -1 para sair:''')
    
    num = int(input())

    if num == -1:
        break

    plot_weighted_graph_from_dataset(num)
