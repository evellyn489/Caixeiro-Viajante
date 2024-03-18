import dijkstra

def read_matrix_distance(name_file):
    with open(name_file, 'r') as file:
        matrix_distance = [list(map(int, line.split())) for line in file.readlines()]

    return matrix_distance

def print_matrix_distance(matrix_distance):
    for x in matrix_distance:
        print(x)

while True:
    print('='*5 + " PCV " + "="*5)
    print('''\n1 - att48
2 - dantzig42
3 - fri26
4 - gr17
5 - p01

Escolha qual base de dados deseja selecionar ou -1 para sair:''')
    
    num = int(input())

    if num == -1:
        break

    name_file = ""

    if num == 1:
        name_file = "./datasets/att48.txt"

    elif num == 2:
        name_file = "./datasets/dantzig42.txt"

    elif num == 3:
        name_file = "./datasets/fri26.txt"

    elif num == 4:
        name_file = "./datasets/gr17.txt"

    elif num == 5:
        name_file = "./datasets/p01.txt"

    else:
        print("Não existe essa opção. Selecione um número entre 1 e 5.")
        continue

    matrix_distance = read_matrix_distance(name_file)
    print('\nBASE SELECIONADA\n')

    print('''Qual algoritmo você deseja rodar?
          A - Força Bruta
          B - Algoritmo de Dijkstra
          C - Algoritmo de Kruskal
          D - Algoritmo de Christofides
          E - SAIR''')
    
    option = input().upper()
    
    if option == 'A':
        print('Força bruta')
    elif option == 'B':
        print('Dijkstra')
    elif option == 'C':
        print('Kruskal')
    elif option == 'D':
        print('Christofides')
    elif option == 'E':
        break
    else:
        print("Não existe essa opção. Selecione uma letra entre A e E.")
