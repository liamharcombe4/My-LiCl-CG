import numpy as np

def write_matrix_to_file(matrix, file_path):
    '''Writes a matrix to a text file.'''
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def main():

    var = 0.07

    with open('coord.txt', 'r') as file:
        coords = np.array([[float(num) for num in line.split()] for line in file])

    scaled_coords = np.sqrt(1 - var)*coords
    noise = np.random.normal(0, np.sqrt(var), coords.shape)
    noisy_coords = scaled_coords + noise

    write_matrix_to_file(noisy_coords, 'coord.raw')
    write_matrix_to_file(-noise, 'force.raw')

if __name__ == "__main__":
    main()