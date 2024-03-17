mport itertools
import time

bases_de_dados = {
    "ATT48": [
        (6734, 1453), (2233, 10), (5530, 1424), (401, 841),
        (3082, 1644), (7608, 4458), (7573, 3716), (7265, 1268),
        
    ],
    "DANTZIG42": [
        (0, 0), (0, 5), (0, 8), (0, 13),
        (0, 17), (2, 2), (2, 5), (2, 8),
        
    ],
    "FRI26": [
        (0, 0), (0, 2), (0, 4), (0, 6),
        (0, 8), (2, 0), (2, 2), (2, 4),
        
    ],
    "GR17": [
        (20833.3333, 17100.0000), (20900.0000, 17066.6667),
        (21300.0000, 13016.6667), (21600.0000, 14150.0000),
        (21600.0000, 14966.6667), (21600.0000, 16500.0000),
        (22183.3333, 13133.3333), (22583.3333, 14300.0000),
        
    ],
    "P01": [
        (0, 0), (1, 2), (3, 1), (5, 2),
        (4, 4), (6, 5), (7, 6), (8, 7),
        
    ]
}

def distancia(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def calcular_custo(rota):
    custo = 0
    for i in range(len(rota) - 1):
        custo += distancia(rota[i], rota[i + 1])
    custo += distancia(rota[-1], rota[0])  # Voltando ao ponto inicial
    return custo

def forca_bruta_pcv(pontos):
    menor_custo = float('inf')
    melhor_rota = None
    for rota in itertools.permutations(pontos):
        custo_rota = calcular_custo(rota)
        if custo_rota < menor_custo:
            menor_custo = custo_rota
            melhor_rota = rota
    return melhor_rota, menor_custo

def executar_algoritmo_para_base_de_dados(nome_base_de_dados, pontos):
    print(f"Executando algoritmo de força bruta para a base de dados {nome_base_de_dados}...")
    inicio = time.time()
    melhor_rota, menor_custo = forca_bruta_pcv(pontos)
    fim = time.time()
    print(f"Rota encontrada: {melhor_rota}")
    print(f"Custo total da melhor rota: {menor_custo}")
    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print()

for nome_base_de_dados, pontos in bases_de_dados.items():
    executar_algoritmo_para_base_de_dados(nome_base_de_dados, pontos)
