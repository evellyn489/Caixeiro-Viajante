def read_matrix_distance(name_file):
    file = open(name_file, 'r')

    matrix_distance = []

    for lines in file.readlines():
        line = lines.split()
        matrix_distance.append([int(x) for x in line])

    file.close()

    return matrix_distance

name_file = 'name.txt'

matrix_distance = read_matrix_distance(name_file)

print(matrix_distance)