import numpy as np

def read_matrix_from_file(file_path):
    """Reads a matrix from a text file."""
    with open(file_path, 'r') as file:
        matrix = [[float(num) for num in line.split()] for line in file]
    return np.array(matrix)

def add_gaussian_noise(matrix, mean=0, std=1):
    """Adds Gaussian noise to a matrix."""
    noise = np.random.normal(mean, std, matrix.shape)
    return matrix + noise

def write_matrix_to_file(matrix, file_path):
    """Writes a matrix to a text file."""
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def main():
    input_file = 'coord.txt'  # Replace with your input file name
    output_file = 'force.txt' # Replace with your desired output file name
    mean = 0     # Mean of the Gaussian noise
    std = 1      # Standard deviation of the Gaussian noise

    # Read, process, and write the matrix
    matrix = read_matrix_from_file(input_file)
    noisy_matrix = add_gaussian_noise(matrix, mean, std)
    write_matrix_to_file(noisy_matrix, output_file)

if __name__ == "__main__":
    main()
