def read_matrix_distance(name_file):
    with open(name_file, 'r') as file:
        matrix_distance = [list(map(int, line.split())) for line in file.readlines()]

    return matrix_distance

def print_matrix_distance(matrix_distance):
    for x in matrix_distance:
        print(x)

while True:
    print('''\nEscolha qual base de dados quer selecionar ou -1 para sair:
1 - att48
2 - dantzig42
3 - fri26
4 - gr17
5 - p01''')
    
    num = int(input())

    if (num == -1):
        break

    name_file = ""

    if (num == 1):
        name_file = "./datasets/att48.txt"

    elif (num == 2):
        name_file = "./datasets/dantzig42.txt"

    elif (num == 3):
        name_file = "./datasets/fri26.txt"

    elif (num == 4):
        name_file = "./datasets/gr17.txt"

    elif (num == 5):
        name_file = "./datasets/five.txt"

    else:
        print("Não existe essa opção. Selecione um número entre 1 e 5.")

    if (1 <= num <= 5):
        matrix_distance = read_matrix_distance(name_file)
        print_matrix_distance(matrix_distance)