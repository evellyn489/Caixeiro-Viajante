def read_matrix_distance(name_file):
    with open(name_file, 'r') as file:
        matrix_distance = [list(map(int, line.split())) for line in file.readlines()]

    return matrix_distance


name_file = './datasets/att48.txt'
matrix_distance = read_matrix_distance(name_file)

print(matrix_distance)
