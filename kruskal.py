import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Graph: 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 

    def read_adjacency_matrix(self, filename):
        adjacency_matrix = np.loadtxt(filename, dtype=int)
        num_vertices = adjacency_matrix.shape[0]

        self.V = num_vertices

        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = int(adjacency_matrix[u][v])
                if weight != 0:
                 self.addEdge(u, v, weight)

        

    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 

    def find(self, parent, i): 
        if parent[i] != i: 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    def union(self, parent, rank, x, y): 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
        else: 
            parent[y] = x 
            rank[x] += 1

    def KruskalMST(self): 
        result = [] 
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2]) 
        parent = [] 
        rank = [] 
        
        print(self.V)

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        while e < self.V - 1: 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 

            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 

        minimumCost = 0
        print("Edges in the constructed MST") 
        for u, v, weight in result: 
            minimumCost += weight 
            print("%d -- %d == %d" % (u, v, weight)) 
        print("Minimum Spanning Tree", minimumCost) 
        
        G = nx.Graph()

        # Add edges to the graph
        for u, v, weight in result:
            G.add_edge(u, v, weight=weight)

        # Draw the graph
        pos = nx.spring_layout(G)  # positions for all nodes
        nx.draw(G, pos, with_labels=True, node_color='pink', node_size=150, edge_color='k', linewidths=5, font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Show the graph
        plt.title("Minimum Spanning Tree")
        plt.show()


if __name__ == '__main__': 
    g = Graph(0)
    g.read_adjacency_matrix("datasets/fri26.txt")
    g.KruskalMST()
