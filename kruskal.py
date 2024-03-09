from unionfind import unionfind

def load_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            node1, node2, cost = parts[0], parts[1], int(parts[2])
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append((cost, node1, node2))
            graph[node2].append((cost, node2, node1))
    return graph

def load_edges(G):
    num_nodes = 0
    edges = []

    for _, value in G.items(): 
        num_nodes += 1
        edges.extend(value)

    return num_nodes, sorted(edges)

def kruskals(G):
    total_cost = 0
    MST = []

    num_nodes, edges = load_edges(G)
    uf = unionfind(num_nodes)

    for edge in edges:
        cost, n1, n2 = edge[0], edge[1], edge[2]

        if not uf.issame(conv_char(n1), conv_char(n2)):
            total_cost += cost
            uf.unite(conv_char(n1), conv_char(n2))
            MST.append((n1, n2, cost))

    return MST, total_cost

def conv_char(c):
    return int(c)

def main():
    # Substitua 'seu_arquivo.txt' pelo caminho do seu arquivo de dados
    graph_file = "datasets/att48.txt"
    G = load_graph_from_file(graph_file)
    MST, total_cost = kruskals(G)

    print(f'Minimum spanning tree: {MST}')
    print(f'Total cost: {total_cost}')

main()