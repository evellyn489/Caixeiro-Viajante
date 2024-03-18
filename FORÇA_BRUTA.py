import itertools
import numpy as np
import time

class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def addEdge(self, u, v, weight):
        if u not in self.adjacencias:
            self.adjacencias[u] = []
        self.adjacencias[u].append((v, weight))

    def read_adjacency_matrix(self, filename):
        adjacency_matrix = np.loadtxt(filename, dtype=int)
        num_vertices = adjacency_matrix.shape[0]

        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = int(adjacency_matrix[u][v])
                if weight != 0:
                    self.addEdge(u, v, weight)

    def calcular_distancia(self, caminho):
        distancia_total = 0
        for i in range(len(caminho) - 1):
            v_atual = caminho[i]
            v_prox = caminho[i + 1]
            for v, weight in self.adjacencias[v_atual]:
                if v == v_prox:
                    distancia_total += weight
                    break
        # Adiciona a distância do último vértice de volta ao inicial
        v_final = caminho[-1]
        v_inicial = caminho[0]
        for v, weight in self.adjacencias[v_final]:
            if v == v_inicial:
                distancia_total += weight
                break
        return distancia_total

    def forca_bruta_pcv(self):
        vertices = list(self.adjacencias.keys())

        menor_distancia = float('inf')
        melhor_caminho = None

        start_time = time.time()

        for i, permutacao in enumerate(itertools.permutations(vertices)):
            distancia = self.calcular_distancia(permutacao)
            if distancia < menor_distancia:
                menor_distancia = distancia
                melhor_caminho = permutacao
            # Exibe o tempo decorrido a cada 10000 iterações
            if i % 10000 == 0:
                current_time = time.time()
                elapsed_time = current_time - start_time
                print("Iteração:", i, "| Tempo decorrido:", elapsed_time, "segundos")

        end_time = time.time()
        execution_time = end_time - start_time

        return melhor_caminho, menor_distancia, execution_time

# Exemplo de uso
grafo = Grafo()
grafo.read_adjacency_matrix('p01.txt')
melhor_caminho, menor_distancia, tempo_execucao = grafo.forca_bruta_pcv()
print("Melhor caminho:", melhor_caminho)
print("Menor distância:", menor_distancia)
print("Tempo de execução:", tempo_execucao, "segundos") 
      
